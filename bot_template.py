import praw
import pdb
import re
import os

BOT_NAME = 'botname'
SUBREDDITS = 'subreddit1+subreddit2'
# LOG_FILE = 'reply.log'

# Create the Reddit instance and log in
reddit = praw.Reddit(BOT_NAME)
subreddit = reddit.subreddit(SUBREDDITS)

# For reply to any comment
for submission in subreddit.hot(limit=10):
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        # print(comment.body)
        # Do a case insensitive search
        if re.search(r"whateverregex", comment.body + ' ', re.IGNORECASE):
            # Reply to the comment
            # comment.reply("Comment reply")
            print("Submission ID: {}, Comment: '{}'".format(submission.id, comment.body))

