import praw
import time

reddit = praw.Reddit('bot')
subred = reddit.subreddit('College_Prestige')

def tradePost(position, price, buy):
    side = "bought" if buy else "sold"
    subred.submit(position+' '+side+' at '+price+' on '+time.ctime(time.time()))
    print('Posted to Reddit!')