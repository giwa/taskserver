from bs4 import BeautifulSoup

# 2to3 conpatibility
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class WebModel:
    def __init__(self, url, body, http_status, content_type, content_length):
        self._http_response_body = body
        self._http_status = http_status
        self._content_type = content_type
        self._content_length = content_length
        self._url = url

    @property
    def host(self):
        """

        :rtype str
        """
        template = "{scheme}://{netloc}"
        o = urlparse(self._url)
        host = template.format(scheme=o.scheme, netloc=o.netloc)
        return host

    @property
    def links(self):
        """
        Return link in a html file
        if href is relative path, convert it to absolute path

        :rtype list[str]
        """
        # TODO: implement using ds4

    @property
    def html(self):
        return self._http_response_body

    @property
    def text(self):
        """
        Return text after remove html tag
        """
        # TODO: implement using ds4

    @property
    def wakachi(self):
        """
        Return parsed text file with wakachi gaki
        """
        # TODO: implement using mecab

    @property
    def http_status(self):
        """
        Return http status code

        :rtype int
        """
        return self._http_status

    @property
    def content_type(self):
        """

        :rtype str
        :return: content type
        """
        return self._content_type

    @property
    def content_length(self):
        """

        :rtype int
        """
        return self._content_length

    @property
    def hashed_url(self):
        """

        :rtype str
        :return:
        """
        # TODO : implment using hashlib

    def __len__(self):
        if self.content_length():
            return self.content_length()
        if self._http_response_body:
            return len(self._http_response_body)

    @staticmethod
    def from_requests_response(resp):
        """

        :rtype WebModel
        :param resp:
        :return:
        """
        w = WebModel(resp.url, resp.text, resp.status_code,
                resp.headers.get("content-type"),
                resp.headers.get("content-length"))
        return w

    @staticmethod
    def from_requests_error():
        # TODO: implement
        pass

