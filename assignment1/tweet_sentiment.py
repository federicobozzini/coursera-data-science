import sys
import json


def hw():
    print 'Hello, world!'
    

def lines(fp):
    print str(len(fp.readlines()))
    
def getTweets(fp):
    tweets = []
    for line in fp:
        tweet = json.loads(line)
        if 'text' in tweet:
            tweets.append(tweet)
    return tweets
    
def rateTweets(tweets, scores):
    tweet_scores = []
    for tweet in tweets:
        tweet_score = 0
        words = tweet['text'].split()
        for term in words:
            term_score =scores.get(term, 0)
            tweet_score+=term_score
        tweet_scores.append(tweet_score)
    return tweet_scores
    

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
    
def generateOutput(tweet_scores):
    for tweet_score in tweet_scores:
        print tweet_score

debug = False
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = getScores(sent_file)
    tweets = getTweets(tweet_file)
    tweet_scores = rateTweets(tweets,scores)
    if debug:
        lines(sent_file)
        lines(tweet_file)
        printScores(scores)
        printTweets(tweets)
        print tweet_scores
        
    generateOutput(tweet_scores)

if __name__ == '__main__':
    main()
