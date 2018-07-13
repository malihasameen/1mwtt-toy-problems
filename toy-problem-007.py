"""
  * http://www.pythonchallenge.com/pc/def/peak.html
  * Python Challenge Level 5
"""

# peakhell sound like pickel (python object serialization)
import urllib.request
import pickle

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(html)
for line in data:
    print("".join(k*v for k,v in line))
