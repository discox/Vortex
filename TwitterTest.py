#import twython
#from nltk.twitter import Twitter
from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile


# need to set the environment variable: export TWITTER="/home/mpeyron/Vortex/twitter-files"

tw = Twitter()


#tw.tweets(keywords='Donald, Trump', limit=10) #looks for keywords

#tw.tweets(follow=['759251', '612473'], to_screen=True, limit=10) #looks for CNN and BBC

#a = tw.tweets(keywords='Clinton, Trump',follow=['759251', '612473'], limit=10)

oauth = credsfromfile()
client = Query(**oauth)

tweets = client.search_tweets(keywords='qnst', limit=1)
#tweet = next(tweets)

tweet = next(tweets)
from pprint import pprint
pprint(tweet, depth=1)
#print tweets

#for tweet in tweets:
#    print tweet['text']
#    print tweet['created_at']
#    print tweet['user']








