#!/usr/bin/env python
''' simply browser '''
import urllib.request


url = urllib.request.urlopen('http://127.0.0.1:80')
for line in url:
    print(line.decode().strip())

