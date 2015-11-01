from datetime import datetime

from interop.models.http_communication_model import HTTPCommunicationModel
from interop.http_filter import HttpFilter
from interop.common.logging.logger_factory import LoggerFactory


class BrowsingHistory:
    def __init__(self, callback, timeout=10):
        self._logger = LoggerFactory.create_logger(self)
        self._http_comms = {}
        self._timeout = timeout  # Seconds
        self._counter = 0
        self._filters = HttpFilter()
        self._callback_f = callback

    def add_http_result(self, http_result):
        http_comm = self.to_http_comm(http_result)

        key = http_comm.five_tuple_key
        if http_result.pattern == 'GET':
            http_comm.uri = http_result.result
            self._http_comms[key] = http_comm

        if http_result.pattern == 'Host:':
            if key not in self._http_comms:
                return

            if self._http_comms[key].stream_id == http_comm.stream_id:
                self._http_comms[key].host = http_result.result

        if http_result.pattern == 'Content-Type:':
            if key not in self._http_comms:
                return

            if is_request_and_response_pair(self._http_comms[key], http_comm):
                self._http_comms[key].content_type = http_result.result

        if http_result.pattern == '<title':
            if key not in self._http_comms:
                return

            if is_request_and_response_pair(self._http_comms[key], http_comm):
                self._http_comms[key].title = http_result.result

                # Check http comm is valid or not
                if self._is_http_comm_valid(key):
                    if self._apply_filters(self._http_comms[key]):
                        self._callback_f(self._http_comms[key])
                del self._http_comms[key]

        self._gc_manager()

    def add_http_result_without_filter(self, http_result):
        http_comm = self.to_http_comm(http_result)

        key = http_comm.five_tuple_key
        if http_result.pattern == 'GET':
            http_comm.uri = http_result.result
            self._http_comms[key] = http_comm

        if http_result.pattern == 'Host:':
            if key not in self._http_comms:
                return

            if self._http_comms[key].stream_id == http_comm.stream_id:
                self._http_comms[key].host = http_result.result
                self._callback_f(self._http_comms[key])

        self._gc_manager()

    def _gc_manager(self):
        self._counter += 1
        if self._counter > 100000:
            self._gc()
            self._counter = 0

    @staticmethod
    def to_http_comm(http_result):
        """
        convert HttpResult to HttpCommnication
        """
        return HTTPCommunicationModel(http_result.id, http_result.src_ip,
                                      http_result.dst_ip, http_result.src_port,
                                      http_result.dst_port, http_result.timestamp,
                                      http_result.stream_id)

    def _is_http_comm_valid(self, key):
        http_comm = self._http_comms[key]
        if not http_comm.is_valid():
            return False

        if not http_comm.content_type == 'text/html':
            return False

        if not http_comm.title:
            return False

        return True

    def _apply_filters(self, http_comm):
        if not self._filters.url(http_comm.url):
            return False

        if not self._filters.title(http_comm.title):
            return False

        return True

    def _gc(self):
        current_time = datetime.now()
        gc_keys = []

        for key, http_comm in self._http_comms.items():
            d = current_time - http_comm.created_at
            if d.total_seconds() > self._timeout:
                gc_keys.append(key)

        for key in gc_keys:
            del self._http_comms[key]

        self._logger.info("{0} record are deleted".format(len(gc_keys)))

def is_request_and_response_pair(request, response):
    """
        Check if they are request and response pair
        dst and src ip and dst and src port would be opposite

        >>> x = HTTPCommunicationModel(1, '2.2.2.2', '1.1.1.1', 1234, 80, '2014/1/1 00:00:00', 1)
        >>> y = HTTPCommunicationModel(1, '1.1.1.1', '2.2.2.2', 80, 1234, '2014/1/1 00:00:00', 2)
        >>> is_request_and_response_pair(x, y)
        True
    """
    if not isinstance(request, HTTPCommunicationModel) or \
            not isinstance(response, HTTPCommunicationModel):
        return False

    if request.src_ip == response.dst_ip and\
       request.dst_ip == response.src_ip and\
       request.src_port == response.dst_port and\
       request.dst_port == response.src_port:
        return True
