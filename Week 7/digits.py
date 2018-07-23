#!/usr/bin/env python3


import sys
import time


userinput = input()
newstring = ""

start = time.time()
for i in userinput:
    if i.isdigit():
        if int(i) < 5:
            newstring+=("<")
        elif int(i) > 5:
            newstring+=(">")
        else:
            newstring+=(i)
    else:
        newstring+=(i)

end =time.time()

print(newstring)
print (end-start)
