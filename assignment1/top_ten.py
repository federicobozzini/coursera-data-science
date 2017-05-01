import sys
import json
from collections import Counter
import operator


def hw():
    print 'Hello, world!'
    

def lines(fp):
    print str(len(fp.readlines()))
    
def getTweets(fp):
    tweets = []
    for line in fp:
        tweet = json.loads(line)
        #if 'text' in tweet and tweet['lang'] == u'en':
        if 'text' in tweet:
            tweets.append(tweet)
    return tweets
    
def hashtag_freqs(tweets):
    hashtags = [hashtag['text'] for tweet in tweets for hashtag in tweet['entities']['hashtags']]
    hashtag_len = len(hashtags)
    weighted_hashtags = Counter(hashtags)
    sorted_h = sorted(weighted_hashtags.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_h
    

def getScores(fp):
    scores = {} # initialize an empty dictionary
    for line in fp:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores
    
    
def printScores(scores):
    print scores.items()
    #for term,score in scores.iteritems():
    #    print term + '-' + str(score) # Print every (term, score) pair in the dictionary
    
def printTweets(tweets):
    print tweets[0]
    

debug = False
    
def main():
    tweet_file = open(sys.argv[1])
    
    tweets = getTweets(tweet_file)
    weighted_hashtags = hashtag_freqs(tweets)
    if debug:
        printTweets(tweets)
    
    #print weighted_hashtags
    for h in weighted_hashtags[0:10]:
        print h[0] + ' ' + str(h[1])  
      
    
        

if __name__ == '__main__':
    main()
