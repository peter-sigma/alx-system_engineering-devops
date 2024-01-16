#!/usr/bin/python3
"""
0-subs.py
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'My-User-Agent'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        results = response.json()
        return results.get('data').get('subscribers')
    except requests.RequestException as e:
        print("Error making API request: {}".format(e))
        print("Response content: {}".format(response.content))
        return 0
    except Exception as e:
        print("Error: {}".format(e))
        return 0

if __name__ == "__main__":
    if len(sys.argv) == 2:
        subreddit_name = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print("The subreddit '{}' has {} subscribers.".format(subreddit_name, subscribers_count))
    else:
        print("Usage: python script_name.py subreddit_name")

