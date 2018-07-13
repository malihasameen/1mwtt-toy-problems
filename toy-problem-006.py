"""
  * http://www.pythonchallenge.com/pc/def/linkedlist.html
  * Python Challenge Level 4
"""

import urllib.request
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
num = "12345"
while True:
    content = urllib.request.urlopen(uri % num).read().decode()
    print(content)
    match = re.search("and the next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

# Divide by two and keep going
num = 16044 / 2
while True:
    content = urllib.request.urlopen(uri % num).read().decode()
    print(content)
    match = re.search("and the next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)



