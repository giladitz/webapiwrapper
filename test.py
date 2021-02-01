import json
from pprint import pprint
from webapiwrapper import WebApiWrapper


j = {
        'description': 'Fixing a hole in the wall',
        'creator_id': 'cus_123456',
        'assigned_to_tradie_id': 'trd_121314',
        'date': '14/12/2020',
        'time': '14:00-16:00'
    }
wapi = WebApiWrapper('http://127.0.0.1:5000/?jid=2', data=json.dumps(j))
wapi.post_req()

user_input = input()

url = 'https://www.abbreviations.com/services/v2/syno.php'
api_keys = {'uid': '8028', 'tokenid': 'SUfOzKkhyYIb575s'}

web_api = WebApiWrapper(url, api_keys=api_keys, extra={'word': user_input, 'format': 'json'})

status, ret_json = web_api.get_req()
synonyms = list()
for item in ret_json:
    item_list = [word.strip() for word in item['synonyms'].split(',')]
    synonyms += item_list

synonyms = set(synonyms)
pprint(synonyms)
''' print them all
if status:
    for items in ret_json:
        print('{:-^100}'.format(''))
        for k, v in items.items():
            print('{} : {}'.format(k, v))
        print('{:*^100}'.format(''))

else:
    print('Error with request: {}'.format(ret_json))
'''