#!/usr/bin/env python3

import copy

L = [[1  ,2 ,3 ,4 ,5],
     [6  ,7 ,8 ,9,10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25]
     ]

x = copy.deepcopy(L)
#temp=copy.deepcopy(L[::-1])

for i in range(len(L)):
    for j in range(len(L)):
        temp=x[::-1][j][i]
        L[i][j]=temp
        #print(x[i][j])

for i in L:
    print(i)

#for i in range(5):
#    print(L[i])
    
