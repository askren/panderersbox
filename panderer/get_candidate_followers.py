import candidates
import logging
import json
import time
import tweepy

import configuration
import tweet_parser
from panderer.build_database_model import User, Tweet, UserToCand
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

engine=create_engine(configuration.get_engine_string())

db_session = scoped_session(sessionmaker(bind=engine))


auth=tweepy.OAuthHandler(configuration.twitter_consumer_key,configuration.twitter_consumer_secret)
auth.set_access_token(configuration.twitter_key, configuration.twitter_secret)

appauth=tweepy.AppAuthHandler(configuration.twitter_consumer_key,configuration.twitter_consumer_secret)

api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
appapi=tweepy.API(appauth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#api=tweepy.API(auth)

def process_user(first_record,cand_name,cand_party):
    if db_session.query(User).filter(User.user_id == first_record.user.id).count() == 0:
        u = User(user_id=first_record.user.id,
            screen_name=first_record.user.screen_name,
            location=first_record.user.location,
            user_desc=first_record.user.description,
            verified=first_record.user.verified,
            followers_count=first_record.user.followers_count,
            friends_count=first_record.user.friends_count,
            list_count=first_record.user.listed_count,
            favorite_count=first_record.user.favourites_count,
            tweet_count=first_record.user.statuses_count,
            user_lang=first_record.user.lang)
        db_session.add(u)
        db_session.flush()

        uc=UserToCand(user_id=first_record.user.id, candidate=cand_name, party=cand_party)
        db_session.add(uc)
        db_session.commit()

def process_tweets(user_tweets):
    all_user_tokens=[]
    for tweet in user_tweets:
        if db_session.query(Tweet).filter(Tweet.tweet_id == tweet.id).count() == 0:
            tweet_content, hashtag_content = tweet_parser.lem_tweet_tokens(tweet.text)
            t = Tweet(tweet_id=tweet.id,
                  tweet_text=tweet.text,
                  tweet_record=tweet._json,
                  tweet_content=tweet_content,
                  hashtag_content=hashtag_content,
                  in_reply_to_status_id=tweet.in_reply_to_status_id,
                  in_reply_to_user_id=tweet.in_reply_to_user_id,
                  favorited=tweet.favorited,
                  retweeted=tweet.retweeted,
                  lang=tweet.lang,
                  user_id=tweet.user.id)
            db_session.add(t)
            db_session.flush()
            if tweet_content:
                all_user_tokens.extend(tweet_content)

#    with open(configuration.text_dir + str(user_tweets[0].user.id) +'_tokenized_terms.txt','w') as f:
 #         f.write(' '.join(all_user_tokens))

    if all_user_tokens:
        user_record=db_session.query(User).filter_by(user_id=current_user).first()
        user_record.user_content=all_user_tokens

    db_session.commit()

def get_user_tweets(user_id,cand_name,cand_party):
    user_tweets=[]
    #200 is the maximum allowed count
    new_tweets = appapi.user_timeline(user_id=user_id,include_rts=True,count=200)
    user_tweets.extend(new_tweets)
    #save the id of the oldest tweet less one
    oldest = user_tweets[-1].id - 1
    #keep grabbing tweets until we get to 1080 tweets
    for i in range(0,5):
        #all subsequent requests use the max_id param to prevent duplicates
        new_tweets = appapi.user_timeline(user_id=user_id,count=200,include_rts=True,max_id=oldest)
        if len(new_tweets) == 0:
            break
        #save most recent tweets
        user_tweets.extend(new_tweets)
        #update the id of the oldest tweet less one
        oldest = user_tweets[-1].id
    process_user(user_tweets[0],cand_name,cand_party)
    process_tweets(user_tweets)

def check_friendship(user_id,candidate_handles,cand_name,cand_party):
    for handle in candidate_handles:
        friendship=api.show_friendship(source_id=user_id,target_screen_name=handle)
        if friendship[0].following:
            get_user_tweets(user_id,cand_name,cand_party)

def get_tweets(querystring,candidate_handles,cand_name,cand_party):
    query = '%s -RT' %(querystring)
    logger.info("Here's your query: %s",querystring)
    max_tweets = 1080
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=query,count=100, lang='en').items(max_tweets)]
    for item in searched_tweets:
        user_id=item.user.id
        if db_session.query(User).filter(User.user_id == user_id).count() == 0:
            try:
                check_friendship(user_id,candidate_handles,cand_name,cand_party)
            except:
                logger.exception("Failed to process: %s", user_id)

def main():
    for candidate in candidates.all_candidates.values():
        logger.info("Working on candidate: %s", candidate.surname)
        TaggedHash=['#'+tag for tag in candidate.hashtags]
        joinstr=' OR '
        querystring=joinstr.join(TaggedHash)
        get_tweets(querystring, candidate.handles, candidate.surname,candidate.party)

if __name__ == "__main__":
    main()