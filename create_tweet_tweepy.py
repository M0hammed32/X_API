import tweepy
import os
# Replace these values with your own credentials


API_KEY = os.environ.get('API_KEY')
API_KEY_SECRET = os.environ.get('API_KEY_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.environ.get('BEARER_TOKEN')

# Authenticate to Twitter using OAuth 2.0 Bearer Token
client = tweepy.Client(bearer_token=BEARER_TOKEN, 
                       consumer_key=API_KEY, 
                       consumer_secret=API_KEY_SECRET, 
                       access_token=ACCESS_TOKEN, 
                       access_token_secret=ACCESS_TOKEN_SECRET)

# Post a tweet
tweet = "بــسم الله الرحمن الرحــــيم"
response = client.create_tweet(text=tweet)

print("Tweet posted successfully!", response)