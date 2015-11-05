import json

from test.rest_test_suite import RestTestSuite


class FilesAPITest(RestTestSuite):

    def test_create(self):
        data = {
                'name': self.faker.name(),
                'kind': self.faker.name(),
                'uri': self.faker.domain_name(),
                'task_id': self.task.id,
                'web_id': self.web.id
                }
        r = self.client.post("/files", data=json.dumps(data))
        self.assertEqual(r.status_code, 201)

    def test_get_file(self):
        r = self.client.get("/files/{}".format(self.file.id))
        self.assertEqual(r.status_code, 200)

        j = json.loads(r.data.decode("utf-8"))
        self.assertEqual(j['name'], self.file.name)
