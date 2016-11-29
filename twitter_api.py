import tweepy
import pprint
def gettweets(search):
    auth=tweepy.OAuthHandler('PugvBL3IsCeqSynV3tExZbHXJ','UTeZCzXfiIrKpC8zIXRGiukOF02iPSxRuBCuB38QyyUqlaRz18')
    auth.set_access_token('2200399648-Fo9CxzzwgZqZAoQKofOjrBqWbLq88Eupvktzoa4','FfdvhDk3ZcJJJrPjljW5vU5lqsdHoo08S9DVqNIMjh19p')

    twitter_api = tweepy.API(auth)

    glitter_tweets = twitter_api.search(
        q=search
    )
    return glitter_tweets
#for tweet in glitter_tweets:
    #pprint.pprint(tweet.user.name + ": " + tweet.text)
