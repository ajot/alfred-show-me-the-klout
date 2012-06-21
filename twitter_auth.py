import tweepy

# Get your Twitter consumer_key, consumer_secret, access_token and access_token_secret from https://dev.twitter.com/apps
consumer_key="your_consumer_key"
consumer_secret="your_consumer_secret"
access_token="your_access_token"
access_token_secret="your_access_token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)