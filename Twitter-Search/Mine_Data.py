import tweepy
from tweepy import OAuthHandler
import json


def process_or_store(tweet):
    json.dumps(tweet)


consumer_key=""
consumer_secret=""
access_token=""
access_secret=""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def Query_tweets(api,query):
    for tweet in  tweepy.Cursor(api.search,
                           q=query,
                           rpp=1000,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items(10):
        process_or_store(tweet._json)
        return status


def find_friends(api):
    for status in  tweepy.Cursor(api.friends).items(10):
        process_or_store(status._json)
    return status

def user_tweets(api,user):
    #for tweet in tweepy.Cursor(api.user_timeline(screen_name=user,count=200)).items(10):
    #    print(tweet)
    new_tweets = api.user_timeline(screen_name=user, count=5, tweet_mode="extended")
    for tweet in new_tweets:
        process_or_store(tweet)
    return tweet





if __name__=="__main__":
    user_tweets(api,'GoogleDevsIN')






