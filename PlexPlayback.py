#!/usr/bin/python
import subprocess
import sys
try:
    from plexapi.server import PlexServer

except:
    print('\033[91mERROR:\033[0m PlexAPI is not installed.')
    x = input("Do you want to install it? y/n:")
    if x == 'y':
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'PlexAPI==4.2.0'])
        from plexapi.server import PlexServer
    elif x == 'n':
        sys.exit()

import re
import requests
import yaml
from urllib.parse import quote_plus, urlencode
import datetime

from plexapi import media, utils, settings, library
from plexapi.base import Playable, PlexPartialObject
from plexapi.exceptions import BadRequest, NotFound

from argparse import ArgumentParser
import os
import random
import pathlib
from configparser import *

with open('config.yml', 'r') as file:
    doc = yaml.load(file, Loader=yaml.SafeLoader)
    x = bool(1)
    y = bool(1)
    session = requests.Session()
    session.verify = False
    requests.packages.urllib3.disable_warnings()
    plex = PlexServer(doc["Plex"]["url"], doc["Plex"]["token"], session, timeout=None)
    plex.settings.get('forceAutoAdjustQuality').set(x)
    plex.settings.get('allowHighOutputBitrates').set(y)
    print(plex.settings.get('forceAutoAdjustQuality').value)
    print(plex.settings.get('allowHighOutputBitrates').value)
plex.settings.save()
