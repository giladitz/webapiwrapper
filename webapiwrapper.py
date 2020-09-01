import re
import requests


class WebApiWrapper:
    """ Abstract class for desired API wrapper needs"""

    def __init__(self, url, api_keys={}, **kwargs):
        self.url = url
        self.api_keys = api_keys
        self.params = kwargs['extra']
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
        print('self.params: {}'.format(self.params))
        response = requests.get(self.url, params=self.params)
        if response.ok is False:
            status = False
            response = {'status code': response.status_code}
            return status, response
        try:
            ret_error = response.json()['error']
        except:
            ret_error = False
        if ret_error is not False:
            return False, ret_error
        return True, response.json()['result']
