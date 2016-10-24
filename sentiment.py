from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentences = ["very bad opinion", "not really sure", "awesome example"]

sid = SentimentIntensityAnalyzer()

for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    print(ss)

    #for k in sorted(ss):
    #    print '{0}: {1}, '.format(k, ss[k]) , end=''

    #print()

