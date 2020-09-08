from webapiwrapper import WebApiWrapper
from colorama import init, Fore, Back, Style


init()
coloring_schema = [Fore.LIGHTBLUE_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.LIGHTRED_EX, Fore.LIGHTRED_EX]

MAX_COUNT = 18

while True:
    url = 'https://www.abbreviations.com/services/v2/syno.php'
    api_keys = {'uid': '8028', 'tokenid': 'SUfOzKkhyYIb575s'}

    print(Fore.WHITE + "\n\nEnter a word to search for its Synonyms: ")
    input_word = input()
    web_api = WebApiWrapper(url, api_keys=api_keys, extra={'word': input_word, 'format': 'json'})
    status, ret_json = web_api.get_req()
    if not status:
        print('{color} Word: "{word}" did not work, try another!'.format(color=Fore.RED, word=input_word))
        continue
    synonyms = list()
    antonyms = list()
    for item in ret_json:
        try:
            if isinstance(item, str):
                if item == 'synonyms':
                    item_synonyms = [word.strip() for word in ret_json[item].split(',')]
                    synonyms += item_synonyms
            elif isinstance(item, dict):
                check = item.get('synonyms', None)
                if check is not None:
                    if len(item['synonyms']) > 0:
                        item_synonyms = [word.strip() for word in item['synonyms'].split(',')]
                        synonyms += item_synonyms
                check = item.get('antonyms', None)
                if check is not None:
                    if len(item['antonyms']) > 0:
                        item_antonyms = [word.strip() for word in item['antonyms'].split(',')]
                        antonyms += item_antonyms
        except:
            print('Do not have a rule for item: {}, type: {}'.format(item, type(item)))

    synonyms = set(synonyms)
    antonyms = set(antonyms)
    counter = MAX_COUNT
    i = 0
    for ele in synonyms:
        counter -= 1
        try:
            print(coloring_schema[i % len(coloring_schema)] + ele)
            i += 1
        except:
            pass

        if counter == 0:
            print(Fore.WHITE + "What's next?")
            what_next = input()
            if what_next == "/":
                counter = 9
            else:
                break