#!/usr/bin/python3
"""
Recursively finds all hot posts from an API
"""
import json
import requests
import sys


def recurse(subreddit, hot_list=[], after="", count=0):
    stuff = {'User-Agent':
             'Mozilla/5.0'}
    link = "https://www.reddit.com/r/"
    if after == "":
        info = requests.get('{}{}/hot.json?limit=1'.format(
            link, subreddit), allow_redirects=False, headers=stuff)
    else:
        info = requests.get(
            '{}{}/hot.json?limit=1&after={}&count={}'.format(
                link, subreddit, after, count),
            allow_redirects=False, headers=stuff)
    if info.status_code == 200:
        info = info.json()
        if len(info.get('data').get('children')) == 0:
            return hot_list
        post = info.get('data').get('children')[0].get('data')
        title = post.get('title')
        after = info.get('data').get('after')
        count = count + 1
        hot_list.append(title)
        if after is not None:
            return (recurse(subreddit, hot_list, after, count))
        else:
            return (hot_list)
    else:
        return(None)
