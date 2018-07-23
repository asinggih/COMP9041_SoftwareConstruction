#!/usr/bin/env python3

import sys

def error():
    print ("Usage: {} <number of lines> <string>".format(sys.argv[0]))

if len(sys.argv) != 3:
    print (error())
    sys.exit()

else:
    print("blob")
    if sys.argv[1].isdigit() == False:
        print ("{}: argument 1 must be a non-negative integer".format(sys.argv[0]))
    else:
        for i in range(int(sys.argv[1])):
            print(sys.argv[2])

