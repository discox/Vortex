from nltk.twitter import Twitter

# need to set the environment variable: TWITTER=/home/mat/PycharmProjects/ScanX/twitter-files

tw = Twitter()

#tw.tweets(keywords='Donald, Trump', limit=10)

tw.tweets(follow=['759251', '612473'], to_screen=True, limit=10)
