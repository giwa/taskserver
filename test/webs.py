import json

from test.rest_test_suite import RestTestSuite


class WebsAPITest(RestTestSuite):

    def test_create(self):
        data = {'url': self.faker.url(),
                'http_status': 200,
                'title': self.faker.name(),
                'host': self.faker.domain_name(),
                'kind': self.faker.name(),
                'task_id': self.task.id
                }
        r = self.client.post("/webs", data=json.dumps(data))
        self.assertEqual(r.status_code, 201)
