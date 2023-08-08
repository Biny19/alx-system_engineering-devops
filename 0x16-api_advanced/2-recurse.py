#!/usr/bin/python3
"""
A list containing the titles of all hot articles for a given subreddit
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """A function returning top ten post titles recursively"""
     url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Biny19@alxswe.com"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for ch in results.get("children"):
        hot_list.append(ch.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
