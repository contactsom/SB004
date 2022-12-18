import unittest
import requests
import json

class MyTestCase(unittest.TestCase):
    def test_api_get(self):
        resp = requests.get("https://reqres.in/api/users?page=2")
        assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
        for record in resp.json()['data']:
            if record['id'] == 7:
                assert record['first_name'] == "Michael", \
                    "Data not matched! Expected : Michael, but found : " + str(record['first_name'])
                assert record['last_name'] == "Lawson", \
                    "Data not matched! Expected : Lawson, but found : " + str(record['last_name'])

    def test_api_post(self):
        data = {'name': 'John',
                'job': 'QA'}
        resp = requests.post(url="https://reqres.in/api/users", data=data)
        data = resp.json()
        y = json.dumps(data)
        print(y)
        assert (resp.status_code == 201), "Status code is not 201. Rather found : " \
                                          + str(resp.status_code)
        assert data['name'] == "John", "User created with wrong name. \
            Expected : John, but found : " + str(data['name'])
        assert data['job'] == "QA", "User created with wrong job. \
            Expected : QA, but found : " + str(data['name'])



