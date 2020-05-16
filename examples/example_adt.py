'''Module for representing how to work with TweetAnalyser'''

from home_tasks.hometask3.abstract_data_type import TweetAnalyser

analyser = TweetAnalyser('D:/UCU/Програмування/2 семестр/home_tasks/hometask3/TWEET_METADATA.json')
# collecting all retweets
analyser.collect_retweet(original=False, there=False)
# managing what parameters of tweet we will live
analyser.manage_what_live({'created_at', 'text', 'user:name',
                           'user:screen_name', 'retweeted_status:user:name',
                           'retweeted_status:user:screen_name'})
# saving analysed tweets to file
analyser.save('D:/UCU/Програмування/2 семестр/home_tasks/hometask3/analysed_tweets.json')

