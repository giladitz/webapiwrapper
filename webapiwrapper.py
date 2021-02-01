import re
import requests


class WebApiWrapper:
    """ Abstract class for desired API wrapper needs"""

    def __init__(self, url, api_keys={}, prints=False, **kwargs):
        self.url = url
        self.api_keys = api_keys
        self.prints = prints
        self.params = None
        check_key = kwargs.get('extra', None)
        if check_key is not None:
            self.params = kwargs['extra']
        self.data = kwargs.get('data', None)
        if api_keys is not None:
            self.form_api_url()

    def form_api_url(self):
        """ check for existing ?<string>= in url to
        know how to add the API keys sequence
        https://www.abbreviations.com/services/v2/ana.php?uid=8028&tokenid=SUfOzKkhyYIb575s&term=sweet&format=xml"""
        separators = ['&'] * len(self.api_keys)

        match = re.search('(\?\w+=)', self.url)
        try:
            _ = match.group(0)
        except:
            separators[0] = '?'

        for sep, (k, v) in zip(separators, self.api_keys.items()):
            self.url += '{sep}{key}={val}'.format(sep=sep, key=k, val=v)

    def get_req(self):
        # print('self.params: {}'.format(self.params))
        response = requests.get(self.url, params=self.params)
        if self.prints:
            print('"get_req" called and replied with: {}'.format(response.content))
        if response.ok is False:
            status = False
            response = {'status code': response.status_code}
            return status, response
        json_ret = response.json()
        check = json_ret.get('error', None)
        if check is not None:
            return False, check
        check = json_ret.get('result', None)
        if check is not None:
            return True, check

        return False, json_ret

    def post_req(self):
        # print('self.params: {}'.format(self.params))
        response = requests.post(self.url, params=self.params, data=self.data)
        if self.prints:
            print('"post_req" called and replied with: {}'.format(response.content))
        if response.ok is False:
            status = False
            response = {'status code': response.status_code}
            return status, response
        json_ret = response.json()
        check = json_ret.get('error', None)
        if check is not None:
            return False, check
        check = json_ret.get('result', None)
        if check is not None:
            return True, check

        return False, json_ret

    def put_req(self):
        # print('self.params: {}'.format(self.params))
        response = requests.put(self.url, params=self.params)
        if self.prints:
            print('"put_req" called and replied with: {}'.format(response.content))
        if response.ok is False:
            status = False
            response = {'status code': response.status_code}
            return status, response
        json_ret = response.json()
        check = json_ret.get('error', None)
        if check is not None:
            return False, check
        check = json_ret.get('result', None)
        if check is not None:
            return True, check

        return False, json_ret


    def delete_req(self):
        # print('self.params: {}'.format(self.params))
        response = requests.delete(self.url, params=self.params)
        if self.prints:
            print('"delete_req" called and replied with: {}'.format(response.content))
        if response.ok is False:
            status = False
            response = {'status code': response.status_code}
            return status, response
        json_ret = response.json()
        check = json_ret.get('error', None)
        if check is not None:
            return False, check
        check = json_ret.get('result', None)
        if check is not None:
            return True, check

        return False, json_ret

