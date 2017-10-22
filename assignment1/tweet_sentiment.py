import sys
import json
    
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
    for term,score in scores.iteritems():
        print term + ' ' + str(score)
    
def printTweets(tweets):
    for tweets in tweets:
        print tweets

def printTweetScores(tweet_scores):
    for scores in tweet_scores:
        print scores

debug = False
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = getScores(sent_file)
    tweets = getTweets(tweet_file)
    tweet_scores = rateTweets(tweets,scores)
    if debug:
        printScores(scores)
        printTweets(tweets)
        
    printTweetScores(tweet_scores)

if __name__ == '__main__':
    main()
