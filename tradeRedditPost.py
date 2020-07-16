import praw
import time

def tradePost(position, price, buy):
    reddit = praw.Reddit('bot')
    subred = reddit.subreddit('Trading_Activity_rn')
    side = "bought" if buy else "sold"
    subred.submit(position+' '+side+' at '+price+' on '+time.ctime(time.time()))
    print('Posted to Reddit!')