from tweet_researcher import TweetResearcher

researcher = TweetResearcher('standart', path='Hometasks/examples')
researcher.add_keyword('government')
# adding api keys, given to you by Twitter
researcher.add_api_keys((< consumer key >,
                         < consumer secret >,
                         < access token key >,
                         < access token secret >))
researcher.add_other_params({'count': '100', 'until': '2020-05-14'})
researcher.do_research()
