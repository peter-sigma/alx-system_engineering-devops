#!/usr/bin/python3
"""Query subscribers in a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns total number of subscribers in a given subreddit."""
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {
            "User-Agent": "sigma:0x16.api.advanced"
        }
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            return 0
        results = response.json().get("data")
        return results.get("subscribers")
    except (Exception):
        return (0)
