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
        
state_dict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
state_dict = dict((v.upper(),k) for k, v in state_dict.iteritems())

def getState(string):
    if string[-5:] == u', USA':
        state_name = string[:-5]
        return state_dict.get(state_name, u'')
    else:
        state_name = string[-2:]
        if state_name in state_dict.values():
            return state_name
        else:
            return ''
        
def rateTweet(tweet, scores):
    tweet_score = 0
    words = tweet['text'].split()
    for term in words:
        if term in scores:
           term_score =scores.get(term)
           tweet_score+=term_score
    return tweet_score
    
            
def geolocalize_tweets(tweets, scores):
    useful_tweets = [tweet for tweet in tweets if "place" in tweet and tweet['place'] is not None and "full_name" in tweet['place']]
    geo_tweets = [(tweet, getState(tweet['place']['full_name'].upper()), rateTweet(tweet,scores)) for tweet in useful_tweets]
    geo_tweets = [(tweet, state, rate) for (tweet, state, rate) in geo_tweets if state != u'']
    return geo_tweets
        
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
        
    geo_tweets = geolocalize_tweets(tweets, scores)  
    
    #rated_terms = rateNewTerms(new_terms, tweets, tweet_scores)
    #for geo_tweet in geo_tweets:
     #   print geo_tweet[1] + ' ' + str(geo_tweet[2])
    
    gts = {}   
    for geo_tweet in geo_tweets:
        state = geo_tweet[1]
        score = geo_tweet[2]
        if state in gts:
            x = gts[state]
            gts[state] = x[0] + score, x[1]+1
        else:
            gts[state] = (score, 1)
            
    #for state,score in gts.iteritems():
    #    print state + ' ' + str(score)
        
    gts2 = {}
    for state in gts:
        gts2[state] = gts[state][0]/gts[state][1]
        #print state + ' ' + str(gts2[state])
        
    maxScore = -10
    maxState = ''
    for state, score in gts2.iteritems():
        if (score > maxScore):
            maxScore = score
            maxState = state
    print maxState
    
        
    #generateOutput(tweet_scores)

if __name__ == '__main__':
    main()
