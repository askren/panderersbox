import logging
import json
import tweepy

import configuration
import tweet_parser
import candidates
import stopwords


auth=tweepy.OAuthHandler(configuration.twitter_consumer_key,configuration.twitter_consumer_secret)
auth.set_access_token(configuration.twitter_key, configuration.twitter_secret)

api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)



def process_tweets(tweets):
    handle_tokens=[]
    for tweet in tweets:
        tweet_content, hashtag_content = tweet_parser.lem_tweet_tokens(tweet.text)
        kept_tokens=[]
        for token in tweet_content:
            if token not in stopwords.stopset:
                kept_tokens.append(token)
        if kept_tokens:
            handle_tokens.extend(kept_tokens)
    return handle_tokens


def get_candidate_tweets(handle):
    handle_tweets=[]
    #200 is the maximum allowed count
    new_tweets = api.user_timeline(screen_name = handle,include_rts=False,count=200)
    handle_tweets.extend(new_tweets)
    #save the id of the oldest tweet less one
    oldest = handle_tweets[-1].id - 1
    #keep grabbing tweets until we get them all
    for i in range(0,16):
        #all subsequent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=handle,count=200,include_rts=False,max_id=oldest)
        if len(new_tweets) == 0:
            break
        #save most recent tweets
        handle_tweets.extend(new_tweets)
        #update the id of the oldest tweet less one
        oldest = handle_tweets[-1].id
    handle_json = [tweet._json for tweet in handle_tweets]
    handle_tokens=process_tweets(handle_tweets)
    return(handle_json, handle_tokens)

def main():
    for candidate in candidates.all_candidates.values():
        logger.info("Working on candidate: %s", candidate.surname)
        candidate_json=[]
        candidate_tokens=[]
        for handle in candidate.handles:
            handle_json,handle_tokens=get_candidate_tweets(handle)
            candidate_json.extend(handle_json)
            candidate_tokens.extend(handle_tokens)

        with open((configuration.text_dir + 'CandidateMessaging/' + candidate.surname + '_tweets_tokenized.txt'),'w') as f:
            f.write(' '.join(candidate_tokens))

        with open((configuration.text_dir + 'CandidateMessaging/' + candidate.surname + '_tweets.json'),'w') as j:
            for object in candidate_json:
                json.dump(object, j)

if __name__ == "__main__":
    main()