#!/usr/bin/python

import json
import requests
import random


def PickAWinner():
    url = 'https://api.meetup.com/2/rsvps'

    params = dict(
        key='XXXXXXXXXXXXXXXXXXXX', # Replace with your Meetup.com API key
        event_id='YYYYYYYYY', # Replace with your Meetup.com event ID
        order='name'
    )

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    response = resp.text

    # with open('response.json', 'w') as outfile:
    #     json.dump(data, outfile)

    j = json.loads(response.encode('ascii', 'ignore').decode())  # This is a Python Dict (JSON array)
    i = 0
    results = j['results']
    members = dict()
    while i < len(results):
        rsvp = results[i]
        members[i] = str(rsvp['member']['name'])
        i += 1
    return str(random.choice(members))