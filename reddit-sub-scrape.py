import praw, os
# this will automate joining old subreddits after migrating to new account

client_id = str(os.getenv("SR_REDDIT_CLIENTID"))
client_secret = str(os.getenv("SR_REDDIT_SECRET"))
password = str(os.getenv("SR_REDDIT_PWD"))
user_agent = "mac:" + str(os.getenv("SR_REDDIT_CLIENTID")) + ":v1 (by u/" + str(os.getenv("SR_REDDIT_USERNAME")) + ")"
username = str(os.getenv("SR_REDDIT_USERNAME"))


reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent=user_agent,
    username=username,
)

print(reddit.auth.url(scopes=["identity"], state="...", duration="permanent"))

print(reddit.read_only)
# Output: False

# assume you have a praw.Reddit instance bound to variable `reddit`
subreddit = reddit.subreddit("redditdev")

print(subreddit.display_name)
# Output: redditdev
print(subreddit.title)
# Output: reddit development
print(subreddit.description)
# Output: a subreddit for discussion of ...

"""
def get_subreddits():
    "" "
    This function your subreddits and writes it to a text file
    "" "
    my_subs = [subreddit.display_name for subreddit in reddit.user.subreddits(limit=None)]
    print(my_subs)


if __name__ == "__main__":
    get_subreddits()
"""