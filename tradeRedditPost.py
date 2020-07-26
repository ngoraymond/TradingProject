import praw
import time

def login():
    print ("Logging in..")
    try:
        r = praw.Reddit(username = os.environ["reddit_username"],
                password = os.environ["reddit_password"],
                client_id = os.environ["client_id"],
                client_secret = os.environ["client_secret"],
                user_agent = "Reddit Trade_Post Bot 0.1")
        print ("Logged in!")
    except:
        print ("Failed to log in!")
    return r

def tradePost(position, price, buy):
    reddit = login()
    subred = reddit.subreddit('Trading_Activity_rn')
    side = "bought" if buy else "sold"
    subred.submit(position+' '+side+' at '+price+' on '+time.ctime(time.time()))
    print('Posted to Reddit!')