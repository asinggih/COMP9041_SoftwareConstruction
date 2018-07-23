#!/usr/bin/env python3

import sys
import os

argLength=len(sys.argv)

start=1
N=10

try:
    x=int(sys.argv[1])*-1
    if x > 0:
        start = 2
        N = x
    else:
        sys.exit()

except:
    #start=1
    # need to put if else here if no linenumbers are specified, default is 10
    if isinstance(sys.argv[1], str) == False: 
        print("Usage: {} <negative num of lines> <file1> ..... <fileN>".format(os.path.basename(__file__)))
        sys.exit()

for i in range(start,argLength):
    L = []
    try:
        file=open((sys.argv[i]))
    except:
        print ("./{} can't open {}".format(os.path.basename(__file__), sys.argv[i]))
        sys.exit()
    while True:
        line=file.readline()
        if line:
            line = line[:-1]    # remove \n from the end of the file
#            print (line)
            L.append(line)
        else:
            break
    
    file.close()
    limit = len(L)
    startIdx = limit-N
    
    if argLength > 2: 
        print ("==> {} <==".format(sys.argv[i]))


    if limit < 10:
        for i in L:
            print(i)
    else:
        for i in range(startIdx, limit):
            print(L[i])

    L=[]
