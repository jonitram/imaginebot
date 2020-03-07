import tweepy
import os
import pickle

def login():

    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    client = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        client.verify_credentials()
    except Exception as e:
        raise e
    return client
    
def load_pickle(input_file, default):
    try:
        result = pickle.load( open( input_file, "rb" ) )
    except (OSError, IOError):
        result = default
    return result

def save_pickle(output_file, input_value):
    pickle.dump( input_value, open( output_file, "wb" ) )
    return