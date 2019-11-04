import requests
import json

class RunMain():

    # def __init__(self, url, method, data=None, headers=None):
    #     self.t = self.run_main(url, method, data, headers)

    def send_get(self, url, data, headers):
        res = requests.get(url=url, params=data, headers=headers, timeout=10)
        result = res.json()
        return json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)

    def send_post(self, url, data, headers):
        Ares = requests.post(url=url, params=data, headers=headers, timeout=10,)
        result = Ares.json()
        return json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)


    def run_main(self, url, method, data=None, headers=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data, headers)
        else:
            res = self.send_post(url, data, headers)
        return res

if __name__ == "__main__":
    url = "https://www.v2ex.com/api/nodes/show.json?name=python"

    test = RunMain()
    print(test.run_main(url, 'GET',))
