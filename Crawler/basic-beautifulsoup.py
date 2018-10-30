# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:28:16 2018

@author: Kritika Mishra
"""

from bs4 import BeautifulSoup

import requests

url = "www.amazon.in"

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))