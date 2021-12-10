import tweepy
import json
import pandas as pd
from datetime import datetime
import Figure

#key from twiter app
api_key = "daCs6GBNjuMO0YQx6kKFpKjtV"
api_secret_key = 'SuIUtn1YgIlBcr1AR9Ew5LR61CfIAuJWw0pyJE1K66ktrv5hGR'
access_token = '1866544818-q1QuDE57nZwFGHKGvNKYtdG44JvsMCIAg0RicXN'
access_token_secret ='lFXmd28M8JMsOjCTKiqwfPYD3lVuL9u4WJDHRIf9gMG1Z'

#access API
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#check if date is the same date
def same_date(d1, since):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    since = datetime.strptime(since, "%Y-%m-%d")
    diff = (d1 - since).days
    if diff == -1:
        return True
    else:
        return False
    
user = input("twitter username : @")

output = []
since = input('show tweets from? YYYY-MM-DD until now:')
for tweet in tweepy.Cursor(api.user_timeline, id=user, tweet_mode="extended").items():
    text = tweet.full_text
    created_at = tweet.created_at
    if same_date(created_at.strftime("%Y-%m-%d"), since):
        break
    line = {'text' : text, 'created_at' : created_at.strftime('%Y-%m-%d')}
    output.append(line)

df = pd.DataFrame(output)
#df.to_csv('output.csv')

Figure.create_bar(df, user)

# for tweet in hasilUser:
#     print(tweet.created_at)

#print(len(hasilUser))

