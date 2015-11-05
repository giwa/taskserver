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

    def test_get_web(self):
        r = self.client.get("/webs/{}".format(self.web.id))
        self.assertEqual(r.status_code, 200)

        j = json.loads(r.data.decode("utf-8"))
        self.assertEqual(j['url'], self.web.url)
