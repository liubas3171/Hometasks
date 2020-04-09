'''
Module for presentation of features of module json
which was made for comfortable work with .json files
'''

import json

if __name__ == '__main__':
    # reading json file
    with open('example_of_usage_api.json', 'r', encoding='utf-8', ) as file:
        data = json.load(file)

    dct = {}
    for tweet in range(len(data['statuses'])):
        # making dict with key - name of user and value - text of his tweet
        dct[data['statuses'][tweet]['user']['name']] = data['statuses'][tweet]['text']

    # writing new created json in file
    with open('dumped_json_file.json', 'w', encoding='utf-8') as fl:
        json.dump(dct, fl, ensure_ascii=False, indent=4)

    # example of pretty print
    print(json.dumps(data, indent=4))
