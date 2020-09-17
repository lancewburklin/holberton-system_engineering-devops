#!/usr/bin/python3
"""
Gets the top 10 hot posts on a subreddit
"""
import json
import requests
import sys


def top_ten(subreddit):
    count = 1
    stuff = {'User-Agent':
             'Mozilla/5.0'}
    info = requests.get('https://www.reddit.com/r/{}/hot.json'.format(
        subreddit), allow_redirects=False, headers=stuff)
    if info.status_code == 200:
        for items in info.json().get('data').get('children'):
            if count < 11:
                for thing in items.values():
                    if type(thing) is not str and thing.get('title'):
                        count += 1
                        print(thing.get('title'))
    else:
        print("None")
