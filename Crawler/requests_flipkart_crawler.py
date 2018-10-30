# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:39:23 2018

@author: Kritika Mishra
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:33:47 2018

@author: Kritika Mishra
"""

from requests import get
url="https://www.flipkart.com/search?q=laptop&otracker=start&as-show=off&as=off"
response = get(url)
print(response.text[:5000])