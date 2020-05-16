'''Module for representing how to work with TweetAnalyser'''

import TweetAnalyser

analyser = TweetAnalyser('Hometasks/examples/TWEET_METADATA.json')
# collecting all retweets
analyser.collect_retweet(original=False, there=False)
# managing what parameters of tweet we will keep
analyser.manage_what_live({'created_at', 'text', 'user:name',
                           'user:screen_name', 'retweeted_status:user:name',
                           'retweeted_status:user:screen_name'})
# saving analysed tweets to file
analyser.save('Hometasks/examples/analysed_tweets.json')
