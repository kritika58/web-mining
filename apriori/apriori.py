import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  
from apyori import apriori  

dataset = [['HotDogs','Buns','Ketchup'],['HotDogs','Buns'],['HotDogs','Coke','Chips'],['Chips','Coke'],['Chips','Ketchup'],['HotDogs','Coke','Chips']]
print("Given Dataset:")
print('--------------------------')
for i in dataset:
    for j in i:
        print(j + ' | ', end="")
    print('\n--------------------------')
ar = apriori(dataset, min_support=0.35, min_confidence=0.6, min_lift=1, max_length=3)  
result = list(ar)  
lofr = len(result)
finalres=[]
for i in result:
    for j in i[2]:
        finalres.append([j,i[1]])

finalres.reverse()
print("\n\n")

for i in finalres:
    p = i[0]
    item=[ x for x in p]
    if(len(item[0])>0):
        x1, *_ = item[0]
    else:
        x1="Null"
    if(len(item[1])>0):
        x2, *_ = item[1]
    else:
        x2="Null"
    print('\n\n--------------------------------')
    print("Association rule: " + x1 + " -> " + x2 )
    print("Confidence: " + str(i[0][2]))
    print("Support: " + str(i[1]))
    print("Lift: " + str(i[0][3]))
    print('--------------------------------')
    print()
