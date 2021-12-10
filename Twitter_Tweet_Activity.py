import tweepy
import json
import pandas as pd
from datetime import datetime
import Figure

#key from twiter app
api_key = ""
api_secret_key = ''
access_token = ''
access_token_secret =''

#access API
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#check if date is the same date
def same_date(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    diff = abs((d2 - d1).days)
    if diff > 0:
        return False
    else:
        return True
    

#hasilUser = api.user_timeline(id="jokowi", count=10000)
#tweets = tweepy.Cursor(api.user_timeline, id="jokowi", until='2021-11-01').items()

output = []
since = '2021-12-01'
for tweet in tweepy.Cursor(api.user_timeline, id="jokowi", tweet_mode="extended").items():
    text = tweet.full_text
    created_at = tweet.created_at
    if same_date(created_at.strftime("%Y-%m-%d"), since):
        break
    line = {'text' : text, 'created_at' : created_at.strftime('%Y-%m-%d')}
    output.append(line)

df = pd.DataFrame(output)
#df.to_csv('output.csv')
user = 'jokowi'
Figure.create_bar(df, user)

# for tweet in hasilUser:
#     print(tweet.created_at)

#print(len(hasilUser))

