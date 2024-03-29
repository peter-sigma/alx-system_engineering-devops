#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
'''import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")'''


import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "sigma-peApp/1.0 (by sigma-pe)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    print("URL:", url)
    print("Headers:", headers)

    print("Response Headers:", response.status_code)    
    # Check if the response is successful
    if response.status_code != 200:
        print("Status code not ok!!!")
        return 0
    
    try:
        data = response.json()
        # Check if 'data' key exists in the JSON response
        if 'data' in data:
            subscribers = data['data'].get('subscribers', 0)
            return subscribers
        else:
            print("ok but no data to retrieve" )
            return 0
    except Exception as e:
        print("An error occurred:", e)
        return 0


