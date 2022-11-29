#!/usr/bin/python3
"""prints the titles of the first 10
hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """ Queries to reddit API"""
    h = {
        "User-Agent": "mozilla/5.0"
    }
    p = {
        'limit': 10
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=h, params=p, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return
    dict_ = response.json()
    hot_post = dict_['data']['children']
    if len(hot_post) == 0:
        print(None)
        return
    else:
        for post in hot_post:
            print(post['data']['title'])
