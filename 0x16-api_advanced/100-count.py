#!/usr/bin/python3
"""
Function to count words in all hot posts of a given Reddit subreddit
"""
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Prints counts of given words found in hot posts of a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Biny19@alxswe.com"}
    params = {"limit": 100, "after": after}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return
    
    data = response.json().get('data')
    if data is None:
        return
    
    children = data.get('children')
    if children is None:
        return
    
    for child in children:
        title = child.get('data', {}).get('title', "").lower()
        for word in word_list:
            word = word.lower()
            if title.count(' ' + word + ' ') > 0:
                word_count[word] = word_count.get(word, 0) + title.count(' ' + word + ' ')

    after = data.get('after')
    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print("{}: {}".format(word, count))

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)
