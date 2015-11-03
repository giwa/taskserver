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
        r = self.app.post("/files", data=json.dumps(data))
        print(r.data)
        self.assertEqual(r.status_code, 201)
