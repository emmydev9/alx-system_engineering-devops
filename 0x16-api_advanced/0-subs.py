#!/usr/bin/python3
"""A function that returns the number of
subscriber count from a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """ Queries to reddit api"""
    user_agent = "mozilla/5.0"
    header = {
        "User-Agent": user_agent
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=header, allow_redirects=False)

    dict_ = response.json()

    if response.status_code != 200:
        return 0
    if 'data' not in dict_:
        return 0
    if 'subscribers' not in dict_["data"]:
        return 0
    return dict_["data"]["subscribers"]
