import nltk

from nltk.twitter import Twitter

# need to set the environment variable: export TWITTER="/home/cabox/workspace/twitter-files/credentials.txt"

tw = Twitter()


#tw.tweets(keywords='Donald, Trump', limit=10)

tw.tweets(follow=['759251', '612473'], to_screen=True, limit=10)
