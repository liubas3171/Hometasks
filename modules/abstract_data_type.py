'''
Module with class TweetAnalyser which can do some analysis
of tweets which are represented in json format
'''

import json
from linked_list import LinkedList


class TweetAnalyser:
    '''Class for analysing tweets in format json'''

    def __init__(self, path=None):
        '''(TweetAnalyser, str) -> None
        Create a new TweetAnalyser.
        path - absolute path to file where has been saved some data about tweets.
        This file had to be created by TweetResearcher.
        '''
        if path:
            with open(path, 'r', encoding='utf-8') as file:
                self._info = json.load(file)
                self._path = path[:path.rindex('/') + 1]
        else:
            self._info = None
            self._path = None
        self._collected_tweets = LinkedList()

    def add_path(self, path):
        '''str -> None
        Add path to TweetAnalyser.
        path - absolute path to file where has been saved some data about tweets.
        This file had to be created by TweetResearcher.
        '''
        with open(path, 'r', encoding='utf-8') as file:
            self._info = json.load(file)
            self._path = path[:path.rindex('/') + 1]

    def give_tweets(self):
        '''Return LinkedList with tweets that have been added to TweetAnalyser'''
        return self._collected_tweets

    def add_all(self):
        '''
        Put all tweets that were collected at computer by TweetResearcher to TweetAnalyser.
        Works only path to metadata was specified
        to TweetAnalyser (with initiation or add_path() method)
        '''
        res = LinkedList()
        for tweet in self.iter_by_files():
            res.add(tweet)
        self._collected_tweets = res

    def add_tweets(self, tweets):
        '''dict -> None
        Adds tweets from dict to TweetAnalyser.
        Parameter tweets should be loaded .json file
        '''
        keyword = 'results' if 'results' in tweets else 'statuses'
        for i in tweets[keyword]:
            self._collected_tweets.add(i)

    def _checker(self):
        '''Raise exception if there are no path to file specified'''
        if not self._info:
            raise Exception('Enter a path to file with metadata')

    def collect_retweet(self, original=True, there=True):
        '''(bool, bool) -> None
        If original = True, only original tweets will be put in TweetAnalyser.
        Otherwise, retweeted posts will be put in TweetAnalyser.
        If param there == True, method considers tweets that have been added to TweetAnalyser.
        Otherwise, tweets saved on computer with help of TweetResearcher will be considered.
        '''
        res = LinkedList()
        if original and there:
            for tweet in self._collected_tweets:
                if not 'retweeted_status' in tweet:
                    res.add(tweet)
        elif not original and there:
            for tweet in self._collected_tweets:
                if 'retweeted_status' in tweet:
                    res.add(tweet)
        elif not original and not there:
            for tweet in self.iter_by_files():
                if 'retweeted_status' in tweet:
                    res.add(tweet)
        elif original and not there:
            for tweet in self.iter_by_files():
                if not 'retweeted_status' in tweet:
                    res.add(tweet)
        self._collected_tweets = res

    def relative_to_acc(self, nickname, mentioned=False, there=True):
        '''(str, bool, bool) -> None
        Put to TweetAnalyser all tweets that are related to person with nickname.
        If mentioned = True, tweets where this person was mentioned will be collected.
        If mentioned = False, tweets made by this person will be collected.
        If param there = True, method considers tweets that have been added to TweetAnalyser.
        Otherwise, tweets saved on computer with help of TweetResearcher will be considered.
        '''
        res = LinkedList()
        if there and not mentioned:
            for tweet in self._collected_tweets:
                if (tweet['user']['name'] == nickname or
                        tweet['user']['screen_name'] == nickname):
                    res.add(tweet)
        elif there and mentioned:
            for tweet in self._collected_tweets:
                if tweet['entities']['user_mentions']:
                    for user in tweet['entities']['user_mentions']:
                        if (user['screen_name'] == nickname or
                                user['name'] == nickname):
                            res.add(tweet)
        elif not there and not mentioned:
            for tweet in self.iter_by_files():
                if (tweet['user']['name'] == nickname or
                        tweet['user']['screen_name'] == nickname):
                    res.add(tweet)
        elif not there and mentioned:
            for tweet in self.iter_by_files():
                if tweet['entities']['user_mentions']:
                    for user in tweet['entities']['user_mentions']:
                        if (user['screen_name'] == nickname or
                                user['name'] == nickname):
                            res.add(tweet)
        self._collected_tweets = res

    def collect_from_location(self, location, there=True):
        '''(str, bool) -> None
        Put to TweetAnalyser all tweets that were made by users registered in given location.
        If param there = True, method considers tweets that have been added to TweetAnalyser.
        Otherwise, tweets saved on computer with help of TweetResearcher will be considered.
        '''
        res = LinkedList()
        if there:
            for tweet in self._collected_tweets:
                if tweet['user']['location'] and location in tweet['user']['location']:
                    res.add(tweet)
        else:
            for tweet in self.iter_by_files():
                if tweet['user']['location'] and location in tweet['user']['location']:
                    res.add(tweet)
        self._collected_tweets = res

    def collect_with_people(self, num_mentioned, there=True):
        '''(int, bool) -> None
        Put to TweetAnalyser all tweets in which were mentioned a given number of people.
        If param there = True, method considers tweets that have been added to TweetAnalyser.
        Otherwise, tweets saved on computer with help of TweetResearcher will be considered.
        '''
        res = LinkedList()
        if there:
            for tweet in self._collected_tweets:
                if len(tweet['entities']['user_mentions']) == num_mentioned:
                    res.add(tweet)
        else:
            for tweet in self.iter_by_files():
                if len(tweet['entities']['user_mentions']) == num_mentioned:
                    res.add(tweet)
        self._collected_tweets = res

    def iter_by_files(self):
        '''
        Iterator which yield all tweets that are saved on computer.
        Path to file with metadata should be specified in self.
        '''
        self._checker()
        for name in self._info['list_names']:
            with open('{}{}'.format(self._path, name), 'r', encoding='utf-8') as file:
                data = json.load(file)
            keyword = 'statuses' if 'statuses' in data else 'results'
            for tweet in data[keyword]:
                yield tweet

    def collect_some_most(self, num_tweets, there=True):
        '''(int, bool) -> None
        Put to TweetAnalyser chosen number of most retweeted tweets.
        If tweet is retweet of post that was made earlier, this post will be taken into account.
        If param there = True, method considers tweets that have been added to TweetAnalyser.
        Otherwise, tweets saved on computer with help of TweetResearcher will be considered.
        '''
        res = LinkedList()
        if there:
            for tweet in self._collected_tweets:
                if 'retweeted_status' in tweet and \
                        tweet['retweeted_status']['retweet_count'] > tweet['retweet_count']:
                    tweet = tweet['retweeted_status']
                if 'quoted_status' in tweet and \
                        tweet['quoted_status']['retweet_count'] > tweet['retweet_count']:
                    tweet = tweet['quoted_status']
                # checking if there is this tweet in results
                check = 0
                for el in res:
                    if tweet['id'] == el['id']:
                        check += 1
                if check == 0:
                    res.add_sorted(tweet, 'retweet_count')
                res.add_sorted(tweet, 'retweet_count')
                if len(res) > num_tweets:
                    res.delete(num_tweets)
        elif not there:
            for tweet in self.iter_by_files():
                if 'retweeted_status' in tweet and \
                        tweet['retweeted_status']['retweet_count'] > tweet['retweet_count']:
                    tweet = tweet['retweeted_status']
                if 'quoted_status' in tweet and \
                        tweet['quoted_status']['retweet_count'] > tweet['retweet_count']:
                    tweet = tweet['quoted_status']
                # checking if there is this tweet in results
                check = 0
                for el in res:
                    if tweet['id'] == el['id']:
                        check += 1
                if check == 0:
                    res.add_sorted(tweet, 'retweet_count')
                res.add_sorted(tweet, 'retweet_count')
                if len(res) > num_tweets:
                    res.delete(num_tweets)
        self._collected_tweets = res

    def give_most_retweeted_accs(self, num_accs, there=True):
        '''(int, bool) -> LinkedList
        Return LinkedList with information about users which tweets were most retweeted.
        num_accs is length of returned list. Each Node of list is dict.
        If param there = True, method considers tweets that have been added to TweetAnalyser.
        Otherwise, tweets saved on computer with help of TweetResearcher will be considered.
        '''
        res = LinkedList()
        bottle = self._collected_tweets
        self.collect_some_most(num_accs, there)
        for i in range(len(self._collected_tweets) - 1, -1, -1):
            res.add(self._collected_tweets[i].value['user'])
        self._collected_tweets = bottle
        return res

    def collect_with_hashtag(self, hashtag='', there=True):
        '''(str, bool) -> None
        Put to TweetAnalyser all tweets with given hashtag.
        If hashtag is not given, put all tweets that have hashtags.
        If tweet is retweet from other post with hashtags, it will be putted too
        If param there = True, method considers tweets that have been added to TweetAnalyser.
        Otherwise, tweets saved on computer with help of TweetResearcher will be considered.
        '''
        res = LinkedList()
        if there:
            for tweet in self._collected_tweets:
                if 'quoted_status' in tweet and 'extended_tweet' in tweet['quoted_status']:
                    if tweet['quoted_status']['extended_tweet']['entities']['hashtags']:
                        if not hashtag and tweet not in res:
                            res.add(tweet)
                            continue
                        for word in tweet['quoted_status'] \
                                ['extended_tweet']['entities']['hashtags']:
                            if word['text'] == hashtag and tweet not in res:
                                res.add(tweet)

                if 'extended_tweet' in tweet:
                    if tweet['extended_tweet']['entities']['hashtags']:
                        if not hashtag and tweet not in res:
                            res.add(tweet)
                            continue
                        for word in tweet['extended_tweet']['entities']['hashtags']:
                            if word['text'] == hashtag and tweet not in res:
                                res.add(tweet)
                if tweet['entities']['hashtags']:
                    if not hashtag and tweet not in res:
                        res.add(tweet)
                        continue
                    for word in tweet['entities']['hashtags']:
                        if word['text'] == hashtag and tweet not in res:
                            res.add(tweet)
        else:
            for tweet in self.iter_by_files():
                if 'quoted_status' in tweet and 'extended_tweet' in tweet['quoted_status']:
                    if tweet['quoted_status']['extended_tweet']['entities']['hashtags']:
                        if not hashtag and tweet not in res:
                            res.add(tweet)
                            continue
                        for word in tweet['quoted_status'] \
                                ['extended_tweet']['entities']['hashtags']:
                            if word['text'] == hashtag and tweet not in res:
                                res.add(tweet)
                if 'extended_tweet' in tweet:
                    if tweet['extended_tweet']['entities']['hashtags']:
                        if not hashtag and tweet not in res:
                            res.add(tweet)
                            continue
                        for word in tweet['extended_tweet']['entities']['hashtags']:
                            if word['text'] == hashtag and tweet not in res:
                                res.add(tweet)
                if tweet['entities']['hashtags']:
                    if not hashtag and tweet not in res:
                        res.add(tweet)
                        continue
                    for word in tweet['entities']['hashtags']:
                        if word['text'] == hashtag and tweet not in res:
                            res.add(tweet)
        self._collected_tweets = res

    def set_boundaries(self, from_date='', to_date=''):
        '''(str, str) -> None
        Sets a time boundaries for tweets in ADT.
        This boundaries will be only for tweets that have been put to TweetAnalyser.
        Tweets that not fit in boundaries will be removed from TweetAnalyser.
        Can set one parameter, or two. Format of parameters - YYYYMMDDHHMM.
        For example, 202003220000 – it is 00:00 of March 22, 2020.
        '''
        res_list = LinkedList()
        if (from_date and len(from_date) != 12) or \
                (to_date and len(to_date) != 12):
            raise Exception('Incorect params')

        months = {'Apr': '04', 'Mar': '03', 'Feb': '02', 'Jan': '01',
                  'May': '05', 'June': '06', 'July': '07', 'Aug': '08',
                  'Sept': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        for tweet in self._collected_tweets:
            # Making date of tweet suitable
            lst = tweet['created_at'].split()
            res = lst[-1] + months[lst[1]] + lst[2]
            res += lst[3].split(':')[0] + lst[3].split(':')[1]

            if from_date and to_date:
                if int(from_date) <= int(res) <= int(to_date):
                    res_list.add(tweet)
            elif not to_date and not from_date:
                return None
            elif from_date:
                if int(from_date) <= int(res):
                    res_list.add(tweet)
            else:
                if int(res) <= int(to_date):
                    res_list.add(tweet)
        self._collected_tweets = res_list
        return None

    def __str__(self):
        '''Return str that represents data from TweetAnalyser in good look'''
        res = ''
        for tweet in self._collected_tweets:
            res += json.dumps(tweet, indent=4, ensure_ascii=False)
        return res

    def manage_what_live(self, parameters):
        '''iterable -> None
        Manage what parameters of tweets in ADT to leave,
        and not specified parameters will be deleted.
        parameters must be a container with names of keys.

        For example, if structure of tweet is next:
        {'tweet': {'user': {'nickname': 'only', 'name': 'yyy'}, 'text': 'batman'}}
        and you want to leave only text and name of user,
        you should set parameters=['tweet:user:name', 'tweet:text'].
        Final tweet will be {'tweet': {'user': {'name': 'yyy'}, 'text': 'batman'}}
        '''
        res = LinkedList()

        for tweet in self._collected_tweets:
            litl_res = dict()
            for key in parameters:
                if len(key.split(':')) == 1:
                    if key in tweet:
                        litl_res[key] = tweet[key]
                elif len(key.split(':')) == 2:
                    high, low = key.split(':')
                    if high in tweet and low in tweet[high]:
                        if high in litl_res:
                            litl_res[high][low] = tweet[high][low]
                        else:
                            litl_res[high] = {low: tweet[high][low]}
                elif len(key.split(':')) == 3:
                    high, mid, low = key.split(':')
                    if high in tweet and mid in tweet[high] and \
                            low in tweet[high][mid]:
                        if high in litl_res and mid in litl_res[high]:
                            litl_res[high][mid][low] = tweet[high][mid][low]
                        else:
                            litl_res[high] = {mid: {low: tweet[high][mid][low]}}
                elif len(key.split(":")) == 4:
                    one, two, three, four = key.split(':')
                    if one in tweet and two in tweet[one] and \
                            three in tweet[one][two] and \
                            four in tweet[one][two][three]:
                        if one in litl_res and two in litl_res[one] and \
                                three in litl_res[one][two]:
                            litl_res[one][two][three][four] = tweet \
                                [one][two][three][four]
                        else:
                            litl_res[one] = {two: {three: {four: tweet \
                                [one][two][three][four]}}}
                # there are no depth more than 4 in files
                elif len(key.split(':')) == 5:
                    one, two, three, four, five = key.split(':')
                    if one in tweet and two in tweet[one] and \
                            three in tweet[one][two] and \
                            four in tweet[one][two][three] and \
                            five in tweet[one][two][three][four]:
                        if one in litl_res and two in litl_res[one] and \
                                three in litl_res[one][two] and \
                                four in litl_res[one][two][three]:
                            litl_res[one][two][three][four][five] = tweet \
                                [one][two][three][four][five]
                        else:
                            litl_res[one] = {two: {three: {four: {five: tweet \
                                [one][two][three][four][five]}}}}
            res.add(litl_res)
        self._collected_tweets = res

    def save(self, path):
        '''str -> None
        Save data from TweetAnalyzer to given file in format json.
        Must be given absolute path to file in format 'DISK:/folder/folder/../name.json'
        '''
        res = {}
        i = 1
        for tweet in self._collected_tweets:
            res[i] = tweet
            i += 1
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(res, file, ensure_ascii=False, indent=4)
