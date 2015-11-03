import unittest
import json

from rest_test_suite import RestTestSuite

class TasksAPITest(RestTestSuite):
    def setUp(self):
        super(TasksAPITest, self).setUp()

    def test_status(self):
        #: :type: flask.Response
        data = dict(name="name", description="desc")
        r = self.app.post("/tasks", data=json.dumps(data))
        self.assertEqual(r.status_code, 201)

        j = json.loads(r.data.decode("utf-8"))
        self.assertEqual(j['name'], data['name'])
        self.assertEqual(j['description'], data['description'])


if __name__ == '__main__':
    unittest.main()
