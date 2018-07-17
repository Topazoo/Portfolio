#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: A class to contain, organize, and analyze Reddit data

    Version: Python 2.7
    Requirements: Spreadsheet.py, Reddit.py, Analyzer.py, praw and openpyxl """

import praw
from collections import Counter
from Reddit import Subreddit, Post, User

class Bot(object):
    """ Class to contain highest-order program operations
        @bot_name - The name of the Praw bot """

    def __init__(self, bot_name='193bot'):

        self.reddit = praw.Reddit(bot_name)

        # Create a list of subreddits
        self.subreddits = []

    def get_subreddits(self):
        """ Get info from the spreadsheet """

        subreddit_obj = Subreddit(name=self.subreddits)
        subreddit_obj.feed = self.reddit.subreddit(self.subreddits[2:])
        subreddit_obj.users = subreddit_obj.feed.subscribers
        self.subreddits = [subreddit_obj]

    def get_posts(self, limit=30, range='year'):
        """ Get a number (limit) of top posts ranging back a range.
             @limit - number of posts to collect
             @range - range of time to get posts from """

        # For all subreddits, collect valid posts
        for subreddit in self.subreddits:
            for post in subreddit.feed.top(range, limit=limit):
                post_object = Post(post)
                if post_object.title and post_object.poster:
                    subreddit.top_posts.append(post_object)


    def get_users(self, user_count=10, comment_count=10):
        """ Get the top users for each subreddit
            @user_count - The number of users to record
            @comment_count - The number of recent comments in a subreddit to record """

        for subreddit in self.subreddits:
            users = {}

            # Record posters of last 1000 comments
            for comment in subreddit.feed.comments(limit=5000):
                if comment.author:
                    if comment.author.name not in users.keys():
                        users[comment.author.name] = 1
                    else:
                        users[comment.author.name] += 1

            counter = Counter(users)
            # Get users that comment most frequently
            for user in counter.most_common(user_count):
                try:
                    # Store as a user object
                    new_user = User(user[0])
                    new_user.profile = self.reddit.redditor(user[0])
                    # Store most recent comments
                    new_user.get_comments(subreddit, comment_count)
                    subreddit.top_posters.append(new_user)
                except:
                    continue