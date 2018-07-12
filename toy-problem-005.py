"""
  * http://www.pythonchallenge.com/pc/def/equality.html
  * Python Challenge Level 3
"""
import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
data = re.findall("<!--(.*?)-->",html, re.DOTALL)[-1]

# pattern: ***AAAbCCC*** * is any non-alpha character
result = "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+",data))
print(result)
