import sqlite3

from interop.models.http_result_model import HTTPResultModel

SELECT_SAVE_RESULT = """\
SELECT id, stream_id, src_ip, src_port, dst_ip, dst_port,
       pattern, timestamp, result
FROM save_result
"""

class HTTPResult:
    def __init__(self, db):
        self._db = db

    def _connect(self):
        con = sqlite3.connect(self._db)
        con.text_factory = lambda x: x.decode('utf-8', errors='ignore')
        return con

    def get_result(self, after=None, limit=None):
        sql = SELECT_SAVE_RESULT

        if after is not None:
            sql += ' WHERE id > {0}'.format(after)

        if limit is not None:
            sql += ' LIMIT {0}'.format(limit)

        con = self._connect()
        with con:
            cursor = con.cursor()
            try:
                cursor.execute(sql)
            except Exception as e:
                return
            for row in cursor.fetchall():
                yield self._format_result(row)

    def _format_result(self, row):
        """

        :rtype HTTPResultModel
        :param row:
        :return:
        """
        return HTTPResultModel(*row)
