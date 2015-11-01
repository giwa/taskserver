import requests

class MetaServerAPI:
    def __init__(self, task_name, end_point=None):
        self._task_name = task_name
        if end_point:
            self._end_point = end_point
        else:
            self._end_point = "http://ss.westlab/api"

    def get(self, uri, params=None, headers=None):
        url = self._end_point + uri
        return requests.get(url, params=params, headers=headers)

    def post(self, uri, data=None, params=None, headers=None):
        url = self._end_point + uri
        return requests.post(url, data=data, params=params, headers=headers)
