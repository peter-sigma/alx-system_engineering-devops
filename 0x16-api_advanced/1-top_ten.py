#!/usr/bin/python3
"""A program to querry first 10 hot posts titles""""

from requests import get


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts in a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params)
    all_data = response.json()

    try:
        data = all_data.get('data').get('children')

        for i in data:
            print(i.get('data').get('title'))

    except:
        print("None")
