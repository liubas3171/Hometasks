'''Main program for doing research'''

import json
from home_tasks.hometask3.abstract_data_type import TweetAnalyser
from home_tasks.hometask3.tweet_researcher import TweetResearcher


def accept_api_keys():
    '''None -> tuple
    Accept api keys from user
    '''
    first = input('Please, enter your API key: ')
    second = input('Please, enter your API secret key: ')
    third = input('Please, enter your Access token: ')
    four = input('Please, enter your Access token secret: ')
    return first, second, third, four


def search(word):
    '''str -> None
    Function accepts inputs from user to research tweets correctly
    '''
    while True:
        if word == 'begin':
            path = input('Enter absolute path to folder where tweets will be saved. \n\
Format of path: DISKNAME:/folder/.../folder \nIf you don`t indicate path, \
Tweets will be saved in folder where this module is.\n')
            api_type = input('Enter type of your api (standart, premium, enterprise):\n')
            if api_type in ('premium', 'enterprise'):
                label = input('Enter your label (you can find it \
in tab "dev environments" on Twitter developer site):\n')
                product = input('Enter your product (30day, fullarchive):\n')
                if product not in ('30day', 'fullarchive'):
                    print('Incorrect product')
                    continue
                researcher = TweetResearcher(api_type, path, product, label)
            elif api_type == 'standart':
                researcher = TweetResearcher(api_type, path)
            else:
                print('Incorrect api type')
                continue
            keys = accept_api_keys()
            researcher.add_api_keys(keys)
            key_word = input('Enter word by which will be looking:\n')
            researcher.add_keyword(key_word)
            other_params = input('Enter other params of seacrh. \
Remember that it depend of type of your API. \n\
Example of input: "count:100, until:2015-07-19".\n\
It is optional.\n')
            if other_params:
                params = {}
                for param in other_params.split(', '):
                    params[param.split(':')[0]] = param.split(':')[1]
                researcher.add_other_params(params)
            researcher.do_research()
        else:
            path = input('Enter a path to file with metadata about \
tweets which was saved during previous search.\n \
Format of path: DISKNAME:/folder/.../folder/TWEET_METADATA.json:\n')
            if not path:
                print('Enter path!')
                continue
            api_keys = accept_api_keys()
            researcher = TweetResearcher('standart')
            researcher.add_api_keys(api_keys)
            researcher.do_research(path)


def checker_there():
    '''None -> bool
    Accept inputs from user
    Return True if next command will be doing with tweets that are in program,
    return False if with those tweets that are on computer
    '''
    while True:
        print('Do this with tweets selected before, or with all tweets from metadata?')
        ans = input('1 - selected before, 2 - all tweets\n')
        if ans == '1':
            return True
        if ans == '2':
            return False
        continue


def reposition_date(date):
    '''str -> int
    Accept date in format Thu Mar 05 10:22:47 +0000 2020
    and return int, which equal to 2020*365*24*60 + 31*24*60 + 5*24*60 + 10*60 + 22
    '''
    months = {'Apr': 30, 'Mar': 31, 'Feb': 28, 'Jan': 31,
              'May': 31, 'June': 30, 'July': 31, 'Aug': 31,
              'Sept': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
    lst = date.split()
    res = int(lst[-1]) * 525600 + int(months[lst[1]]) * 24 * 60 + int(lst[2]) * 24 * 60
    res += int(lst[3].split(':')[0]) * 60 + int(lst[3].split(':')[1])
    return res


def checker_none(analyser):
    '''TweetAnalyser -> bool
    Return True if analyser is empty, False otherwise
    '''
    return len(analyser.give_tweets()) == 0


def analysator():
    '''Function for analysing tweets that were collected with Twitter API'''
    ans = input('Enter a path to file with metadata about tweets. \n\
Format of path: DISK:/folder/.../folder/TWEET_METADATA.json\n>')

    data = 'All analysing is doing locally at program, so saved files will be unchanged\n\n'
    data += 'There are main commands for analysing:\n\n'
    data += 'help - to see all available commands\n'
    data += 'num_retw - to know how many retweets are in collected set\n'
    data += 'num_orig - to know how many original tweets are in collected set\n'
    data += 'amount - to know how many tweets are in collected set. \
It also add all tweets to program.\n'
    data += 'add - to add other json file with tweets which wasn`t collected by this program\n'
    data += 'freq - to know how many tweets from collected were made by minute\n'
    data += 'retw - to collect all retweeted tweets\n'
    data += 'orig - to collect all original tweets\n'
    data += 'from_acc - to collect all tweets from given account\n'
    data += 'from_loc - to collect all tweets from users registered at given location\n'
    data += 'num_men - to collect all tweets with given number of people mentioned\n'
    data += 'acc_ment - to collect all tweets where given account mentioned\n'
    data += 'hash - to collect all tweets with given hashtag\n'
    data += 'most_retw - to collect most retweeted posts\n'
    data += 'set_time - to put time boundaries on tweets\n'
    data += 'params - to select params which you want to save\n'
    data += 'see - to see all saved data\n'
    data += 'save - to save chosen data on computer\n'
    data += 'exit - to exit the program\n'
    print(data)

    analyser = TweetAnalyser(ans)
    while True:
        command = input('\nWhat to do?\n>')
        if command == 'help':
            print(data)
        elif command == 'num_retw':
            if checker_none(analyser):
                analyser.collect_retweet(False, False)
                print(len(analyser.give_tweets()))
            else:
                there = checker_there()
                analyser.collect_retweet(False, there)
                print(len(analyser.give_tweets()))
        elif command == 'num_orig':
            if checker_none(analyser):
                analyser.collect_retweet(True, False)
                print(len(analyser.give_tweets()))
            else:
                there = checker_there()
                analyser.collect_retweet(True, there)
                print(len(analyser.give_tweets()))
        elif command == 'amount':
            if checker_none(analyser):
                analyser.add_all()
                print(len(analyser.give_tweets()))
            else:
                there = checker_there()
                if there:
                    print(len(analyser.give_tweets()))
                else:
                    analyser.add_all()
                    print(len(analyser.give_tweets()))
        elif command == 'add':
            ans = input('Enter path to json file you want to add. \n\
Format of path: DISK:/folder/.../folder/filename.json\n')
            with open(ans, 'r', encoding='utf-8') as file:
                tweet_data = json.load(file)
            analyser.add_tweets(tweet_data)
            print('Done\n')
        elif command == 'freq':
            if checker_none(analyser):
                i = 0
                for tweet in analyser.iter_by_files():
                    if i == 0:
                        minn = reposition_date(tweet['created_at'])
                        maxx = reposition_date(tweet['created_at'])
                    if reposition_date(tweet['created_at']) < minn:
                        minn = reposition_date(tweet['created_at'])
                    if reposition_date(tweet['created_at']) > maxx:
                        maxx = reposition_date(tweet['created_at'])
                    i += 1
                print(i / (maxx - minn))
            else:
                if checker_there():
                    i = 0
                    for tweet in analyser.give_tweets():
                        if i == 0:
                            minn = reposition_date(tweet['created_at'])
                            maxx = reposition_date(tweet['created_at'])
                        if reposition_date(tweet['created_at']) < minn:
                            minn = reposition_date(tweet['created_at'])
                        if reposition_date(tweet['created_at']) > maxx:
                            maxx = reposition_date(tweet['created_at'])
                        i += 1
                    print(i / (maxx - minn))
                else:
                    i = 0
                    for tweet in analyser.iter_by_files():
                        if i == 0:
                            minn = reposition_date(tweet['created_at'])
                            maxx = reposition_date(tweet['created_at'])
                        if reposition_date(tweet['created_at']) < minn:
                            minn = reposition_date(tweet['created_at'])
                        if reposition_date(tweet['created_at']) > maxx:
                            maxx = reposition_date(tweet['created_at'])
                        i += 1
                    print(i / (maxx - minn))
        elif command == 'retw':
            if checker_none(analyser):
                analyser.collect_retweet(False, False)
            else:
                there = checker_there()
                analyser.collect_retweet(False, there)
            print('Done. {} tweets in program'.format(len(analyser.give_tweets())))
        elif command == 'orig':
            if checker_none(analyser):
                analyser.collect_retweet(True, False)
            else:
                there = checker_there()
                analyser.collect_retweet(True, there)
            print('Done. {} tweets in program'.format(len(analyser.give_tweets())))
        elif command == 'from_acc':
            ans = input('Enter a name of account:\n>')
            if checker_none(analyser):
                analyser.relative_to_acc(ans, False, False)
            else:
                there = checker_there()
                analyser.relative_to_acc(ans, False, there)
            print('Done. {} tweets in program'.format(len(analyser.give_tweets())))
        elif command == 'from_loc':
            ans = input('Enter a name of location:\n>')
            if checker_none(analyser):
                analyser.collect_from_location(ans, False)
            else:
                there = checker_there()
                analyser.collect_from_location(ans, there)
            print('Done. {} tweets in program'.format(len(analyser.give_tweets())))
        elif command == 'num_men':
            ans = int(input('Enter a number of people mentioned:\n>'))
            if checker_none(analyser):
                analyser.collect_with_people(ans, False)
            else:
                there = checker_there()
                analyser.collect_with_people(ans, there)
            print('Done. {} tweets in program'.format(len(analyser.give_tweets())))
        elif command == 'acc_ment':
            ans = input('Enter a name of account:\n>')
            if checker_none(analyser):
                analyser.relative_to_acc(ans, True, False)
            else:
                there = checker_there()
                analyser.relative_to_acc(ans, True, there)
            print('Done. {} tweets in program'.format(len(analyser.give_tweets())))
        elif command == 'hash':
            ans = input('Enter a hashtag. \
If you don`t point it, all tweets with hashtags will be collected:\n>')
            if checker_none(analyser):
                analyser.collect_with_hashtag(ans, False)
            else:
                there = checker_there()
                analyser.collect_with_hashtag(ans, there)
            print('Done. {} tweets in program'.format(len(analyser.give_tweets())))
        elif command == 'most_retw':
            ans = int(input('Enter how many most retweeted posts will be saved (a number):\n>'))
            if checker_none(analyser):
                analyser.collect_some_most(ans, False)
            else:
                there = checker_there()
                analyser.collect_some_most(ans, there)
            print('Done. {} tweets in program'.format(len(analyser.give_tweets())))
        elif command == 'set_time':
            print('Enter a time boundaries on tweets which will be analysed.\n\
It works only with those tweets that are in program. \n\
Format of date: YYYYMMDDHHMM, for example: 202003220000 – it is 00:00 of March 22, 2020')
            from_date = input('Enter a minimum date. You may not point it.\n>')
            to_date = input('Enter a maximum date. You may not point it.\n>')
            analyser.set_boundaries(from_date, to_date)
            print('Done. {} tweets in program'.format(len(analyser.give_tweets())))
        elif command == 'params':
            ans = input("Enter which parameters of tweets you want to leave.\n\
For example, if structure of tweet is next:\
{'user': {'nickname': 'only', 'name': 'yyy'}, 'text': 'batman'},\n\
and you want to leave only text and name of user,\
you should write parameters like this:\n\
user:name, text\n>")
            analyser.manage_what_live(ans.split(', '))
            print('Done')
        elif command == 'see':
            print(analyser)
        elif command == 'save':
            ans = input('Enter an absolute path to json file in which you want to save data.\n\
Format of file: DISK:/folder/folder/../name.json\n>')
            analyser.save(ans)
            print('Data was saved.')
        elif command == 'exit':
            exit()
        else:
            print('There are no such command')


if __name__ == '__main__':
    while True:
        print('Hello in program that will help you to save and analyse data about tweets.')
        print('To all was well, you should read and write carefully.\n')
        ANS1 = input('What you want to do? (search, analyse):\n>')
        if ANS1 == 'search':
            ANS2 = input('Do you want to begin or continue collection of data? \
(begin, continue):\n>')
            if ANS2 in ('begin', 'continue'):
                search(ANS2)
            else:
                print('Incorrect input')
                continue
        elif ANS1 == 'analyse':
            analysator()
        else:
            print('Incorrect input')
            continue
