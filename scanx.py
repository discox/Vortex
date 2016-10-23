
#use nltk or tweetstream? or tweepy?

print('importing libraries')

# need to set the environment variable: export TWITTER="/home/mpeyron/Vortex/twitter-files"
from nltk.twitter import Twitter, credsfromfile, Query



tw = Twitter()

########### input parameters ###########

stock_ticker = 'intc' # stock ticker
num_tweets = 10 #max number of tweets
num_auth = 10 #max number of authors
period = 365 #amount of time for model

# length of sliding window in days for input parameters
input_window_length = 7

# length of sliding window in days for output parameters
output_window_length = 1


########### look for all related tweets ###########

print('loading input from twitter')

oauth = credsfromfile()
client = Query(**oauth)

tweets = client.search_tweets(keywords=stock_ticker, limit=num_tweets)

tweet = next(tweets)
from pprint import pprint
pprint(tweet, depth=1)


########### build list of authors ###########

########### get sentiment for each tweet ###########

########### build input vectors ###########

########### extract stock market data ###########

########### build output vectors ###########

########### fit the model to the data ###########

########### test against prediction ###########
