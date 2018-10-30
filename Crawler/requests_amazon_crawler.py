# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:39:19 2018

@author: Kritika Mishra
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:33:47 2018

@author: Kritika Mishra
"""

from requests import get
url="https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=laptops"
response = get(url)
print(response.text[:5000])