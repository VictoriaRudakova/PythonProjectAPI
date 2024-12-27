import requests
import json
from logger.logger import Logger
from src.enums.status_code import StatusCode


class HttpRequest:

    def make_get(self, url, query={}, type=''):
        r = requests.get(url=url, params=query,  verify=False)
        Logger().request_log(url=r.url, method=r.request.method, httpcode=r.status_code, body=r.json())
        assert r.status_code == StatusCode.OK.value
        if type != 'response':
            return r.json()
        else:
            return r

    def make_put(self, url, body):
        r = requests.put(url=url, data=json.dumps(body), headers={'Content-Type': 'application/json'})
        Logger().custom_log(f"PUT REQUEST to {url}, with body: {body}")
        Logger().custom_log(f"RESPONSE with STATUS CODE: {r.status_code} from url : {r.url} body: {r.json()}")
        assert r.status_code == StatusCode.OK.value
        return r.json()

    def make_post(self, url, body):
        r = requests.post(url=url, data=json.dumps(body), headers={'Content-Type': 'application/json'})
        Logger().custom_log(f"POST REQUEST to {url}, with body: {body}")
        Logger().custom_log(f"RESPONSE with STATUS CODE: {r.status_code} from url : {r.url} body: {r.json()}")
        assert r.status_code == StatusCode.CREATED.value
        return r.json()

    def make_delete(self, url):
        r = requests.delete(url=url)
        Logger().custom_log(f"DELETE REQUEST to {url}")
        Logger().custom_log(f"RESPONSE with STATUS CODE: {r.status_code} from url : {r.url}")
        assert r.status_code == StatusCode.NOCONTENT.value
        return True
