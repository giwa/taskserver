import json

from test.rest_test_suite import RestTestSuite


class TasksAPITest(RestTestSuite):

    def test_status(self):
        #: :type: flask.Response
        data = dict(name=self.faker.name_female(), kind=self.faker.last_name_female(), description=self.faker.text())
        r = self.client.post("/tasks", data=json.dumps(data))
        self.assertEqual(r.status_code, 201)

        j = json.loads(r.data.decode("utf-8"))
        self.assertIsInstance(j['id'], int)
        self.assertEqual(j['name'], data['name'])
        self.assertEqual(j['kind'], data['kind'])
        self.assertEqual(j['description'], data['description'])

    def test_get_status(self):
        r = self.client.get("/tasks/{}".format(self.task.id))
        self.assertEqual(r.status_code, 200)

        j = json.loads(r.data.decode("utf-8"))
        self.assertEqual(j['name'], self.task.name)
