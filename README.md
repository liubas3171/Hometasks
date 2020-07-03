## Project name: TwitterAnalyser
## Description:
[Video Previev](https://github.com/liubas3171/Hometasks/blob/master/how_to_use.avi)

Cycle of hometasks from basics of programming, which issue is to collect and analyse data about tweets.

With this program, you can automatilally collect data about some tweets with help of Twitter API. Tweets collect by keywords, and you also can put additional parameters of search, like date, location, language, etc. 

When you collected tweets, you can make some analysis with them, like:
* find all retweets
* find most retweeted posts
* find all posts with hashtags
* find all tweets from given user
* find all tweets from user that was registered on given location
* find frequency of tweets per minute
* etc

More you can read at [Wiki](https://github.com/liubas3171/Hometasks/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%962), but it have been written by Ukrainian language.

It is command-line program.
## Table of Contents:
### On Wiki:
[Домашнє завдання №0](https://github.com/liubas3171/Hometasks/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%960)

[Домашнє завдання №1](https://github.com/liubas3171/Hometasks/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%961)

[Домашнє завдання №2](https://github.com/liubas3171/Hometasks/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%962)

[Домашнє завдання №3](https://github.com/liubas3171/Hometasks/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%963)

[Домашнє завдання №4](https://github.com/liubas3171/Hometasks/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%964)

[Домашнє завдання №5](https://github.com/liubas3171/Hometasks/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%965)

[Тема циклу домашніх завдань](https://github.com/liubas3171/Hometasks/wiki/%D0%A2%D0%B5%D0%BC%D0%B0-%D1%86%D0%B8%D0%BA%D0%BB%D1%83-%D0%B4%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%96%D1%85-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D1%8C)

### Modules of program:
* [modules/abstract_data_type.py](https://github.com/liubas3171/Hometasks/blob/master/modules/abstract_data_type.py) - Module with class TweetAnalyser, which analyses tweets.
* [modules/linked_list.py](https://github.com/liubas3171/Hometasks/blob/master/modules/linked_list.py) - Module with class LinkedList, structure of data for TweetAnalyser.
* [modules/tweet_researcher.py](https://github.com/liubas3171/Hometasks/blob/master/modules/tweet_researcher.py) - Module with class TweetResearcher, which collects tweets.
* [modules/main.py](https://github.com/liubas3171/Hometasks/blob/master/modules/main.py) - Module with main program.
## Installation:
From the command line:
```
$ pip install TwitterAPI
$ git clone https://github.com/liubas3171/Hometasks.git
```
Run Hometasks/modules/main.py and read instructions.

## Usage:
### Preconditions
To get started, you have to have a Twitter API keys. To know how to get it, you can visit [Twitter Developer site](https://developer.twitter.com/en/docs/basics/getting-started).
### Examples
* [examples/first_example.py](https://github.com/liubas3171/Hometasks/blob/master/examples/first_example.py) - example of usage Twitter API
* [examples/example_of_usage_api.json](https://github.com/liubas3171/Hometasks/blob/master/examples/example_of_usage_api.json) - one of files with tweets, saved by program. Program saves 1 file per request
* [examples/example_adt.py](https://github.com/liubas3171/Hometasks/blob/master/examples/example_adt.py) - example of analysing tweets
* [examples/analysed_tweets.json](https://github.com/liubas3171/Hometasks/blob/master/examples/analysed_tweets.json) - analysed by program tweets that were saved in file
* [examples/example_researcher.py](https://github.com/liubas3171/Hometasks/blob/master/examples/example_researcher.py) - example of how to collect tweets with class TweetResearcher
* [examples/TWEET_METADATA.json](https://github.com/liubas3171/Hometasks/blob/master/examples/TWEET_METADATA.json) - example of file with metadata about tweets, created by program during collecting tweets
### For who
I think, this program can be useful for developers, enterprisers or researchers that want to analyse behaviour of people or character and meanings of tweets about some chosen topics.

## Contributing:
Currently, I am a sole contributor of this repository.
## Credits:
* Liubas Nazar, UCU, 2020
## Licence:
MIT License
