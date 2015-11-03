import unittest
import json

from rest_test_suite import RestTestSuite

class StatusAPITest(RestTestSuite):
    def test_status(self):
        #: :type: flask.Response
        r = self.app.get('/status')
        self.assertEqual(r.status_code, 200)

        j = json.loads(r.data.decode("utf-8"))
        d = dict(status="up")
        self.assertEqual(j, d)


if __name__ == '__main__':
    unittest.main()
