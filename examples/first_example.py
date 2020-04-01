'''
Simple module that represents opportunities of Twitter API.
It send request to Twitter, get all tweets that have SEARCH_TERM
at json format , and write it in file.
Use module TwitterAPI from third-party developers.
'''

import json
from TwitterAPI import TwitterAPI

SEARCH_TERM = 'Government'
# there must be keys of your Twitter API
API = TwitterAPI("<consumer key>",
                 "<consumer secret>",
                 "<access token key>",
                 "<access token secret>")

TWEETS = API.request('search/tweets', {'q': SEARCH_TERM, 'until': '2020-03-27', 'count': 100})
with open('example_of_usage_api.json', 'w', encoding='utf-8') as file:
    json.dump(TWEETS.json(), file, indent=4, ensure_ascii=False)

# if uncomment, it will print how many requests you can do for next 15 minutes
# print('\nQUOTA: %s' % r.get_quota())
