#!/usr/bin/python3
"""
0-subs.py
"""
import requests

def number_of_subscribers(subreddit):
    """A function that Queries the Reddit API and returns the number of subscribers"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'New-User-Agent'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
