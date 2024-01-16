#!/usr/bin/python3
"""
0-subs.py
"""
import requests

def number_of_subscribers(subreddit):
    """A function that Queries the Reddit API and returns the number of subscribers"""
    import requests

    subreddit_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "New-User-Agent"},
                            allow_redirects=False)
    if subreddit_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
