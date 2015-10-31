from tempfile import NamedTemporaryFile

from task_server_api import TaskServerAPI
from ss_file_uploader import SsFileUploader


class WebManager:
    def __init__(self, task_name, web):
        self._task_name = task_name
        self._web = web
        self._html_file = None
        self._link_file = None
        self._text_file = None
        self._wakachi_file = None
        self._uploader = SsFileUploader(self._task_name)
        self._api = TaskServerAPI(self._task_name)

    def register_result(self):
        web_id = self._register_web()

        if self._web.http_status < 400:
            self._upload_files(web_id)

    def _register_web(self):
        """
        Register web to meta server. If web already exsits in meta server,
        reuse it.

        return web_id
        """
        # TODO: implement after clean up api in meta server


    def _upload_files(self, web_id):
        """
        Upload files to ss
        """
        self._upload_link_file(web_id)
        self._upload_text_file(web_id)
        self._upload_html_file(web_id)
        self._upload_wakachi_file(web_id)

    def _upload_html_file(self, web_id):
        """
        Write html to a file
        """
        with NamedTemporaryFile(delete=False) as f:
            f.write(self._web.html)
        self._html_file = f.name
        file_name = "%s-%s" % (self._web.hashed_url, "html")
        file_ext = "html"
        self._uploader.upload(self._html_file, file_name, file_ext)

    def _upload_link_file(self, web_id):
        """
        Write links into a file
        """
        with NamedTemporaryFile(delete=False) as f:
            for link in self._web.links:
                f.write(link)
                f.write("\n")
        self._link_file = f.name
        file_name = "%s-%s" % (self._web.hashed_url, "link")
        file_ext = "txt"
        self._uploader.upload(self._link_file, file_name, file_ext)

    def _upload_text_file(self, web_id):
        """
        Remove html tag and write to a file
        """
        with NamedTemporaryFile(delete=False) as f:
            f.write(self._web.text)
        self._text_file = f.name
        file_name = "%s-%s" % (self._web.hashed_url, "text")
        file_ext = "txt"
        self._uploader.upload(self._text_file, file_name, file_ext)

    def _upload_wakachi_file(self, web_id):
        """
        write wachied data to a file
        """
        with NamedTemporaryFile(delete=False) as f:
            for w in self._web.wakachi:
                f.write(w)
                f.write("\n")
        self._wakachi_file = f.name
        file_name = "%s-%s" % (self._web.hashed_url, "wakachi")
        file_ext = "txt"
        self._uploader.upload(self._wakachi_file, file_name, file_ext)
