import sys
import json
from collections import Counter


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
    
def calculate_freqs(tweets):
    terms = [term for tweet in tweets for term in tweet['text'].split()]
    terms_num = len(terms)
    #weighted_terms = [(term, 1) for term in terms]
    weighted_terms = dict([(k, v/terms_num) for k,v in Counter(terms).iteritems()])
    return weighted_terms
    

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
    #weighted_terms = calculate_freqs(tweets)
    if debug:
        printTweets(tweets)
    
    #for key, value in weighted_terms.iteritems():
    #    print key + ' ' + str(float(value))  
      
    
    for tweet in tweets[0:30]:
        print tweet
        #for key, value in tweet.iteritems():
        #    print key + u' ' + str(value)  
        

if __name__ == '__main__':
    main()
