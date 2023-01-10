import tweepy
import time
keys = dict(
        screen_name = '',
        consumer_key = '',
        consumer_secret = '',
        access_token =  '',
        access_token_secret = ''
    )
SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

follow_cnt = 0
keyword = "検索キーワード"
a_cnt = 30

search_results = api.search(q=keyword, count=a_cnt)
for result in search_results:
    if follow_cnt <= a_cnt:
        try:
            screen_id = result.user._json["screen_name"]
            api.create_friendship(screen_id)
            print("{0}をフォローしました。" .format(screen_id))
            time.sleep(2)
            follow_cnt += 1
        except tweepy.error.TweepError:
            print("フォローが失敗しました。")
