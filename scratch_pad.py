print('importing libraries')

# need to set the environment variable: export TWITTER="/home/mpeyron/Vortex/twitter-files"
from nltk.twitter import Twitter, credsfromfile, Query
from sentiment import polarity


tw = Twitter()

########### input parameters ###########

stock_ticker = 'intc' # stock ticker
num_tweets = 5 #max number of tweets
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


########### build nseparate components of input vector ###########

authors = []
sentiments = []

for tweet_obj in tweets:

    #get tweet text sentiment
    tweet_text = tweet_obj['text']
    print(tweet_text)
    p = polarity(tweet_text)
    sentiments.append(p)
    print(p)

    #get user ID
    user = tweet_obj['user']
    user_id = user['id_str']
    print(user_id)
    authors.append(user_id)



print("authors are", authors)
print("sentiments are", sentiments)


# build authors component

list_of_authors = set(authors)
input_authors = []
for auth in authors:
