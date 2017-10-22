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
        if 'text' in tweet and tweet['user']['lang'] == u'en':
            tweets.append(tweet)
    return tweets
    
def rateTweets(tweets, scores):
    tweet_scores = []
    new_terms = []
    for tweet in tweets:
        tweet_score = 0
        words = tweet['text'].split()
        for term in words:
            if term in scores:
                term_score =scores.get(term)
                tweet_score+=term_score
            else:
                if len(new_terms) < 20 and term not in new_terms:
                #if term not in new_terms:
                    new_terms.append(term)
        tweet_scores.append(tweet_score)
    return (tweet_scores, new_terms)
    

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
        
def rateNewTerms(new_terms, tweets, tweet_scores):
    rated_terms = []
    tweets_words = [tweet['text'].split() for tweet in tweets]
    for term in new_terms:
        term_score = 0
        for tweet_words, tweet_score in zip(tweets_words, tweet_scores):
            if term in tweet_words:
                term_score+= tweet_score
        rated_term = term, term_score
        rated_terms.append(rated_term)
    return rated_terms

debug = False
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = getScores(sent_file)
    tweets = getTweets(tweet_file)
    (tweet_scores, new_terms) = rateTweets(tweets,scores)
    if debug:
        lines(sent_file)
        lines(tweet_file)
        printScores(scores)
        printTweets(tweets)
    
    rated_terms = rateNewTerms(new_terms, tweets, tweet_scores)
    for rated_term in rated_terms:
        print rated_term[0] + ' ' + str(float(rated_term[1]))    
        
    #generateOutput(tweet_scores)

if __name__ == '__main__':
    main()
