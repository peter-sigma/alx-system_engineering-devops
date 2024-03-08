#!/usr/bin/python3
"""prints the title of the first 10 hot posts in a given subreddit.

"""
import requests


def top_ten(subreddit):
    '''Returs the title of the first 10 hot posts'''
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {
            "User-Agent": "sigma:0x16.api.advanced",
        }
        response = requests.get(url, headers=headers, allow_redirects=False)
        if (response.status_code == 404):
            print('None')
            return 0
        request = response.json().get('data').get('children')
        for i in range(10):
            print(request[i].get('data').get('title'))
    except Exception:
        return 0
