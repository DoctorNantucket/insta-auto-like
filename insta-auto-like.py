#!/usr/bin/env python

"""
This script will find your latest instagram post and your latest liker, and then like like their
latest post.
"""


import requests
import argparse
import logging
import json
import pprint as p

LOGGER_NAME = "root.insta-auto-like"
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
log = logging.getLogger(LOGGER_NAME)
log.setLevel(logging.INFO)


def url_request(url):
    """
    Make URL request to a given URL.
    :returns:
        - request data
    """
    try:
        log.info("Requesting URL: {}".format(url))
        data = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise
    return json.loads(data.text)


def main():
    # TODO: Gather tokens for API requests automatically via argparse or file read
    # CLIENT_ID = 'd6be8cf1143e47f39046c2d1edb403f1'
    # CLIENT_SECRET = '2bf4d600c14544e59f15571dd17e4e0a'
    ACCESS_TOKEN = '6258048.e029fea.aec314f3e7c04aabb8aaed03c954e087'
    API_URL = 'https://api.instagram.com/v1/'
    post_ids = []
    user_ids = []
    log = logging.getLogger(LOGGER_NAME+".main")

    # Get the last 10 posts so we can check for new likers on those posts.
    post = url_request("{0}users/self/media/recent/?access_token={1}&count=10".format(API_URL, ACCESS_TOKEN))

    p.pprint(len(post))

    # Grab the post id so we can get the likers from it.
    for key in post['data']:
        post_ids.append(key['id'])
        log.info("Post ID is {}".format(key['id']))

    for posts in posts_ids:
        # Create dictionary of Likers.
        likers = url_request("{0}media/{1}/likes?access_token={2}&count=5".format(API_URL, post_id, ACCESS_TOKEN))
        # It looks like the last 'liker' in the dictionary is also the last person to like a given post, so it's safe
        # to say that if we pop that last item from the list.
        p.pprint(likers)
    for i in likers['data']:
        user_ids.append(i['id'])

    # Grab the last user ID from the list.
    last_user_like = user_ids[-1]
    log.info("Last User: {}".format(last_user_like))


if __name__ == '__main__':
    main()
