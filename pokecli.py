#!/usr/bin/env python
"""
pgoapi - Pokemon Go API
Copyright (c) 2016 tjado <https://github.com/tejado>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.

Author: tjado <https://github.com/tejado>
"""

import os
import re
import sys
import json
import time
import struct
import pprint
import logging
import requests
import argparse
import getpass
import tweepy

# add directory of this file to PATH, so that the package will be found
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# import Pokemon Go API lib
from pgoapi import pgoapi
from pgoapi import utilities as util

# other stuff
from google.protobuf.internal import encoder
from geopy.geocoders import GoogleV3
from s2sphere import Cell, CellId, LatLng


log = logging.getLogger(__name__)

def get_pos_by_name(location_name):
    geolocator = GoogleV3()
    loc = geolocator.geocode(location_name, timeout=10)

    log.info('Your given location: %s', loc.address.encode('utf-8'))
    log.info('lat/long/alt: %s %s %s', loc.latitude, loc.longitude, loc.altitude)

    return (loc.latitude, loc.longitude, loc.altitude)

def get_cell_ids(lat, long, radius = 10):
    origin = CellId.from_lat_lng(LatLng.from_degrees(lat, long)).parent(15)
    walk = [origin.id()]
    right = origin.next()
    left = origin.prev()

    # Search around provided radius
    for i in range(radius):
        walk.append(right.id())
        walk.append(left.id())
        right = right.next()
        left = left.prev()

    # Return everything
    return sorted(walk)

def encode(cellid):
    output = []
    encoder._VarintEncoder()(output.append, cellid)
    return ''.join(output)

def init_config():
    parser = argparse.ArgumentParser()
    config_file = "config.json"

    # If config file exists, load variables from json
    load   = {}
    if os.path.isfile(config_file):
        with open(config_file) as data:
            load.update(json.load(data))

    # Read passed in Arguments
    required = lambda x: not x in load
    parser.add_argument("-a", "--auth_service", help="Auth Service ('ptc' or 'google')",
        required=required("auth_service"))
    parser.add_argument("-u", "--username", help="Username", required=required("username"))
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument("-l", "--location", help="Location", required=required("location"))
    parser.add_argument("-d", "--debug", help="Debug Mode", action='store_true')
    parser.add_argument("-t", "--test", help="Only parse the specified location", action='store_true')
    parser.set_defaults(DEBUG=False, TEST=False)
    config = parser.parse_args()

    # Passed in arguments shoud trump
    for key in config.__dict__:
        if  key in load and config.__dict__[key] == None:
            config.__dict__[key] = str(load[key])
    config.__dict__['twitter'] = load['twitter']

    if config.__dict__["password"] is None:
        log.info("Secure Password Input (if there is no password prompt, use --password <pw>):")
        config.__dict__["password"] = getpass.getpass()

    if config.auth_service not in ['ptc', 'google']:
      log.error("Invalid Auth service specified! ('ptc' or 'google')")
      return None

    return config

def poke_id2detail(id):
    url = "https://raw.githubusercontent.com/giginet/pokedex/master/dex/dex{0}.json".format(id)
    r = requests.get(url)
    return r.json()

def main():
    # log settings
    # log format
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(module)10s] [%(levelname)5s] %(message)s')
    # log level for http request class
    logging.getLogger("requests").setLevel(logging.WARNING)
    # log level for main pgoapi class
    logging.getLogger("pgoapi").setLevel(logging.INFO)
    # log level for internal pgoapi class
    logging.getLogger("rpc_api").setLevel(logging.INFO)

    config = init_config()
    if not config:
        return

    if config.debug:
        logging.getLogger("requests").setLevel(logging.DEBUG)
        logging.getLogger("pgoapi").setLevel(logging.DEBUG)
        logging.getLogger("rpc_api").setLevel(logging.DEBUG)

    position = get_pos_by_name(config.location)
    if config.test:
        return

    # Twitter
    twitter_auth = tweepy.OAuthHandler(config.twitter['consumer_key'], config.twitter['consumer_secret'])
    twitter_auth.set_access_token(config.twitter['access_token'], config.twitter['access_token_secret'])
    twitter = tweepy.API(twitter_auth)

    # instantiate pgoapi
    api = pgoapi.PGoApi()

    # provide player position on the earth
    api.set_position(*position)

    if not api.login(config.auth_service, config.username, config.password):
        return

    latest_timestamp_ms = int(time.time() * 1000)
    while True:
        # execute the RPC call
        response_dict = api.sfida_action_log().call()
        response = response_dict['responses']['SFIDA_ACTION_LOG']['log_entries']
        newest_response = [el for el in response if el['timestamp_ms'] > latest_timestamp_ms]
        for el in newest_response:
            text = ''
            os.environ['TZ'] = 'Asia/Tokyo'
            time.tzset()
            timestamp = time.strftime("%Y/%m/%d %X", time.localtime(el['timestamp_ms']/ 1000))
            if 'fort_search' in el:
                items_info = el['fort_search']
                items_count = sum([items['count'] for items in items_info['items']])
                text = "ポケストップで {0} 個手に入れた！\n({1})".format(items_count, timestamp)
                twitter.update_status(text)
            elif 'catch_pokemon' in el:
                poke_info = el['catch_pokemon']
                poke_detail = poke_id2detail(poke_info['pokemon_id'])
                temp_filename = '{0}.png'.format(time)
                res = requests.get(poke_detail['image_url'], stream=True)
                with open(temp_filename, 'wb') as image:
                    for chunk in res:
                        image.write(chunk)
                text = "{0} (CP: {1}) を捕まえた！\n({2})".format(
                    poke_detail['name'], poke_info['combat_points'], timestamp)
                twitter.update_with_media(temp_filename, status=text)
                os.remove(temp_filename)
        # print('Response dictionary: \n\r{}'.format(pprint.PrettyPrinter(indent=4).pformat(newest_response)))
        latest_timestamp_ms = max([el['timestamp_ms'] for el in response])
        time.sleep(30)

if __name__ == '__main__':
    main()
