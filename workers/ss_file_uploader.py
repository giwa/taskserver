import requests


class SsFileUploader:
    """
    simple storage file uplaoder
    upload file to ss
    """

    def __init__(self, task_name, end_point=None):
        self._task_name = task_name
        if end_point:
            self._end_point = end_point
        else:
            self._end_point = "http://ss.westlab:8888/api/ss.php"

    def upload(self, file, file_name, file_ext):
        data = dict(
                task_name=self._task_name,
                file_name=file_name,
                file_ext=file_ext
                )
        files = {'file': open(file, 'rb')}
        r = requests.post(self._end_point, files=files, data=data)
        return r

