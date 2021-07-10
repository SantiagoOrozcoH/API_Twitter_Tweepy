# https://docs.tweepy.org/en/stable/getting_started.html

import tweepy
import json
from access_tokens import *

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY_T)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#data = api.me()

data = api.trends_available()

#api.update_status("Hello, twitter! n0b0dy writing this with Python");  #To tweet from python

for num in range(len(data)):
    if(data[num]["name"] == "Colombia"):
        col_id = num
        col_woeid = data[col_id]["woeid"]
        
#print(json.dumps(data[col_id], indent=2))
col_trends = api.trends_place(col_woeid)
print(json.dumps(col_trends[0]["trends"][0], indent=3))     #prints #1 trend in colombia

