'''
Module with class TweetResearcher, which was created to collec
tweets by keyword with usage of Twitter API.
There is used module TwitterAPI from third-party developers.
To install it, enter pip install TwitterAPI to cmd.
'''

import sys
import time
import json
from TwitterAPI import TwitterAPI


class TweetResearcher:
    '''Class for collecting tweets on computer with help of Twitter API'''

    def __init__(self, type_api, path=None, product=None, label=None):
        '''(str, str) -> None
        Create a new TweetResearcher.
        :param path it is absolute path to folder where will be saved tweets.
        path should be in format 'DISK:/folder/../folder'.
        If path is not specified, tweets will be saved to folder where is a module of program.

        :param type_api can be 'standart', 'premium', 'enterprise'.
        If type of your api is premium or enterprise you also
        have to specify product which can be '30day' or 'fullarchive',
        and you have to specify label,
        which is pointed at https://developer.twitter.com/en/account/environments
        '''
        if path:
            self._path = path
        else:
            self._path = sys.path[0]
        if type_api == 'standart':
            self._type_api = type_api
        elif type_api in ('premium', 'enterprise'):
            if not product or not label:
                raise Exception('Enter product and label')
            self._type_api = type_api
            self._product = product
            self._label = label
        else:
            raise Exception('Enter a type of api correctly')
        self._params = dict()
        self._api = None

    def add_api_keys(self, keys):
        '''iterable -> None
        Accept list or tuple with four api keys given by Twitter
        in order: API key, API secret key, Access token, Access token secret.
        They are needed for doing researches.
        '''
        if len(keys) != 4:
            raise Exception('Enter 4 keys')
        self._api = TwitterAPI(keys[0], keys[1], keys[2], keys[3])

    def add_keyword(self, word):
        '''str -> None
        Adds keyword by which tweets will be selected.
        For more info about this words you can visit
        https://developer.twitter.com/en/docs/tweets/search/api-reference/enterprise-search
        '''
        if self._type_api == 'standart':
            key = 'q'
        else:
            key = 'query'
        self._params[key] = word

    def add_other_params(self, params):
        '''dict -> None
        Add dict with other parameters for search.
        This parameters can be different for different types of api.
        Example of params: {'count': '100', "toDate": '201208220000'}.
        About parameters you can read by next links:
        standart api:
        https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets,
        premium api:
        https://developer.twitter.com/en/docs/tweets/search/api-reference/premium-search,
        enterprise api:
        https://developer.twitter.com/en/docs/tweets/search/api-reference/enterprise-search.
        '''
        for key in params.keys():
            self._params[key] = params[key]

    def do_research(self, path_metadata=None):
        '''str -> None
        Do research with installing json files with tweets.
        Before doing this you have to (!) point keyword for search,
        type of api you use and api keys given by twitter.

        If path_metadata isn`t specified, it start install tweets,
        printing how many requests per 15 minutes remain.
        If quota ends, program will sleep 15 minutes and then continue.
        Tweets collect from time this program started work to older.
        For example, first at 15:45, second at 15:30, third at 15:00, etc.
        During work program will write in .json file some metadata about research,
        like parameters and id of next tweets. It will be written in the end of 15-minute quota.

        path_metadata is absolute path to file that have been described above.
        This means that you can interrupt program and then
        start installing from these tweets where you`ve finished.
        Format of path_metadata should be 'DISK:/folder/../folder/name_of_file.json'
        '''
        if not self._api:
            raise Exception('Enter api keys')
        if path_metadata:
            with open(path_metadata, 'r', encoding='utf-8') as file:
                metadata = json.load(file)
            self._params = metadata['params']
            self._type_api = metadata['type_api']
            if self._type_api != 'standart':
                self._label = metadata['label']
                self._product = metadata['product']
        elif not self._params:
            raise Exception('Enter at least keyword')
        else:
            metadata = {'list_names': []}
        start_time = time.time()
        while True:
            try:
                if self._type_api == 'standart':
                    tweets = self._api.request('search/tweets', self._params)
                    self._params['max_id'] = tweets.json()["search_metadata"] \
                                                 ["next_results"].split('=')[1][:-2]
                    key = 'statuses'
                else:
                    tweets = self._api.request('tweets/search/%s/:%s' %
                                               (self._product, self._label), self._params)
                    self._params['next'] = tweets.json()['next']
                    key = 'results'

                # making name of file with tweets
                start = tweets.json()[key][0]['created_at'].split()[1:4]
                start[2] = start[2].replace(':', '_')
                start = '_'.join(start)

                finish = tweets.json()[key][-1]['created_at'].split()[1:4]
                finish[2] = finish[2].replace(':', '_')
                finish = '_'.join(finish)

                name = '{}_____{}'.format(start, finish)
                metadata['list_names'].append('{}.json'.format(name))

                with open('{}/{}.json'.format(self._path, name), 'w', encoding='utf-8') as file:
                    json.dump(tweets.json(), file, indent=4, ensure_ascii=False)

                print('\nQUOTA: %s' % tweets.get_quota())
            except KeyError:
                # saving metadata about saved tweets
                metadata['params'] = self._params
                metadata['type_api'] = self._type_api
                if self._type_api != 'standart':
                    metadata['product'] = self._product
                    metadata['label'] = self._label
                if path_metadata:
                    path = path_metadata
                else:
                    path = '{}/TWEET_METADATA.json'.format(self._path)

                with open(path, 'w', encoding='utf-8') as file:
                    json.dump(metadata, file, indent=4, ensure_ascii=False)
                print('Reloading API, if you want to interrupt process, you can make it now.')
                # 902 is 15 minutes + 2 sec
                time.sleep(902 - (time.time() - start_time))
                start_time = time.time()
            except Exception as exception:
                print('Smt go wrong. Exception: {}'.format(exception))
                exit()
