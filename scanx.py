
import sys
print("the version is")
print(sys.version)

print('checking environment variables')

import os
print(os.environ)

print('test successful')

print('import libraries')

# need to set the environment variable: export TWITTER="/home/mpeyron/Vortex/twitter-files"
# if using pycharm set environment variable with relevant path TWITTER="/Users/mpeyron/PycharmProjects/Vortex/twitter-files"
from nltk.twitter import Twitter, credsfromfile, Query
from sentiment import polarity
import numpy

tw = Twitter()

########### input parameters ###########

stock_ticker = 'qnst' # stock ticker
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


########### build separate components of input vector ###########

print('preparing the data')

authors = []
sentiments = []

for tweet_obj in tweets:

    #get tweet text sentiment
    tweet_text = tweet_obj['text']
    print(tweet_text)
    p = polarity(tweet_text)
    sentiments.append(p)

    #print(p)

    #get user ID
    user = tweet_obj['user']
    user_id = user['id_str']
    #print(user_id)
    authors.append(user_id)



print("authors are", authors)
print("sentiments are", sentiments)

print("there are ", len(authors), " authors")
print("there are ", len(sentiments), "tweets")




# build authors component

list_of_authors = list(set(authors))
input_authors = []


for name in authors:
    tmp_vec = []
    for cursor in list_of_authors:
        if name == cursor:
            tmp_vec.append(1)
        else:
            tmp_vec.append(0)

    input_authors.append(tmp_vec)


print(input_authors)


# prepare input matrix

trunc_input_matrix = numpy.array(input_authors)

trans_sentiments = numpy.transpose(numpy.array([sentiments]))

input_matrix = numpy.append(trunc_input_matrix,trans_sentiments,1)

print (input_matrix)

### note ### still need to add date/timeline


########### extract stock market data ###########

########### build output vectors ###########

########### fit the model to the data ###########

########### test against prediction ###########