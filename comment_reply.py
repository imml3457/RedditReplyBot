#!/usr/bin/python
import praw
import pdb
import re
import os
from datetime import date

today = str(date.today())
today2 = "The current date is: " + today

reddit = praw.Reddit('bot1')

if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

else:
    with open("comments_replied_to.txt", "r") as f:
              comments_replied_to = f.read()
              comments_replied_to = comments_replied_to.split("\n")
              comments_replied_to = list(filter(None, comments_replied_to))

subreddit = reddit.subreddit('CrimzonvaleGitStuff')
for c in subreddit.stream.comments():

    if c.id not in comments_replied_to:

              if re.search("!Date", c.body, re.IGNORECASE):
                  c.reply(today2)
                  print("Replying to: ", c.body)

                  comments_replied_to.append(c.id)

              
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
              
              
    
              
