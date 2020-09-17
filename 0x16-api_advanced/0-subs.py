#!/usr/bin/python3
"""
Get the number of subscribers for a subreddit
"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    stuff = {'User-Agent':
             'Mozilla/5.0'}
    info = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), allow_redirects=False, headers=stuff)
    if info.status_code == 200:
        return (info.json().get('data').get('subscribers'))
    else:
        return (0)
