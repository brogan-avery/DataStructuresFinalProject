'''
Author: Brogan Avery
Date: 2020/10/16
Project Title: ISS API
'''


import json
from urllib.request import urlopen
import bs4
import requests
from bs4 import BeautifulSoup
# import pandas as pd
import re


if __name__ == '__main__':
    response = requests.get("https://www.gps-coordinates.net/id/zion")

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.text

    wordList = re.split("\s", title)

    lat = wordList[5]
    lon = wordList[7]

    lat = lat.rstrip(",")

    print(lat, lon)


