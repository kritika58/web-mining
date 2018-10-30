# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:00:40 2018

@author: Kritika Mishra
"""

import numpy as np
def page_rank(d1,x):
    i=0
    d=np.array([d1])
    g = np.array([[0,0.5,0.5,0,0,0],
                  [0,0,0,0,0,0],
                  [0.67,0.67,0,0,0.67,0],
                  [0,0,0,0,0.5,0.5],
                  [0,0,0,0,0,1],
                  [0,0,0,1,0,0]])
    gt =g.transpose()
    d=[d1]*len(gt)
    for i in range(x):
        l=np.matmul(gt,d)
        d=l
    print(l)
    
print("d= 0.85 and 7 iterations\n")
page_rank(0.85,7)
print("\nd= 0.85 and 100 iterations\n")
page_rank(0.85,100)
print("\nd= 0.85 and 1000 iterations\n")
page_rank(0.85,1000)
print("\nd= 0.86 and 10 iterations\n")
page_rank(0.86,10)
print("\nd= 0.86 and 100 iterations\n")
page_rank(0.86,100)
print("\nd= 0.86 and 1000 iterations\n")
page_rank(0.86,1000)