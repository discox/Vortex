# function to determine the positive vs negative aspect of a sentence


from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()


def polarity(sentence):
    polar = sid.polarity_scores(sentence)
    return polar['compound']









#sentences = ["very bad opinion", "not really sure", "awesome example"]

#sid = SentimentIntensityAnalyzer()

#for sentence in sentences:
#    print(sentence)
#    ss = sid.polarity_scores(sentence)
#    print(ss['compound'])

    #for k in sorted(ss):
    #    print '{0}: {1}, '.format(k, ss[k]) , end=''

    #print()

