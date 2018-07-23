#!/usr/bin/env python3

import sys,re,collections
from urllib.request import urlopen
tag_count = dict()
print(sys.argv[1])
for url in sys.argv[1:]:
    resp = urlopen(url)
    webpage = resp.read().decode('utf-8')
    webpage = re.sub(r'<!--.*?-->','',webpage)
    webpage = re.sub(r'-->','',webpage)
    webpage = webpage.lower()
    for tag in re.findall(r'<\s*(\w+))',webpage):
        print(tag)








