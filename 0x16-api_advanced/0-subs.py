#!/usr/bin/python3
'''
   number_of_subscribers
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        A function that returns the number of subscribers for a given subreddit
    '''
    usr = {'User-Agent': 'sigmapee'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=usr).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
