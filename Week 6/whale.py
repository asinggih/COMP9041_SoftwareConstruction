#!/usr/bin/env python4

import sys
import re

flag=0
if len(sys.argv) == 2:
    track=sys.argv[1]
else:
    flag=1

whales=dict()


userinput=sys.stdin.read()

keyVal=userinput.split('\n')[:-1]

for i in keyVal:
    k=re.findall('\D+', i)
    v=re.findall('\d+', i)

    key=k[0].lstrip(' ').lower()
    key=re.sub('s$', "", key)
    key=re.sub(' +',' ', key)
    value=v[0]

    if key in whales:
        whales[key][0]+=int(value)  # total number
        whales[key][1]+=1           # total pods
    else:
        whales[key]=[int(value)]    # initially create a list, so it can contain total and                                          count
        whales[key].append(1)       # this is appending the count
        
if flag == 0: 
    print("{} observations: {} pods, {} individuals".format(track, whales[track][1], whales[track][0]))
else:
    #for i in whales.sort():
    #    print(i)
    
    keylist = whales.keys()
    for key in sorted(keylist): 
        print("{} observations: {} pods, {} individuals".format(key, whales[key][1], whales[key][0]))






