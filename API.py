import tweepy
import json
import pandas as pd
from datetime import datetime
import Figure

class API(object):

    def __init__(self, username, date):
    #key from twiter app
        self.api_key = ""
        self.api_secret_key = ''
        self.access_token = ''
        self.access_token_secret =''

        #access API
        self.auth = tweepy.OAuthHandler(self.api_key, self.api_secret_key)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

        #get user info
        self.username = username
        self.date = date

    #check if date is the same date
    def same_date(self, d1, since):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        since = datetime.strptime(since, "%d/%m/%Y")
        diff = (d1 - since).days

        if diff == -1:
            return True
        else:
            return False

    def run(self):     
        #user = input("twitter username : @")

        output = []
        #since = input('show tweets from? YYYY-MM-DD until now:')
        for tweet in tweepy.Cursor(self.api.user_timeline, id=self.username, tweet_mode="extended").items():
            text = tweet.full_text
            created_at = tweet.created_at
            check_date = self.same_date(created_at.strftime("%Y-%m-%d"), self.date)
            if check_date:
                break
            line = {'text' : text, 'created_at' : created_at.strftime('%Y-%m-%d')}
            output.append(line)

        df = pd.DataFrame(output)
        #df.to_csv('output.csv')

        Figure.create_bar(df, self.username)

    # for tweet in hasilUser:
    #     print(tweet.created_at)

    #print(len(hasilUser))
