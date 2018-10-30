# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:33:47 2018

@author: Kritika Mishra
"""

from requests import get
url="https://www.imdb.com/search/title?release_date=2018&sort=num_votes,desc&page=1"
response = get(url)
print(response.text[:5000])