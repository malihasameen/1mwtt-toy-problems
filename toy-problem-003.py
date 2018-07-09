"""
  * http://www.pythonchallenge.com/pc/def/map.html
  * Python Challenge Level 1
"""
raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# Beginner Solution
print("Beginner Solution")
result = ""
for c in raw:
    if c.isalpha():
        result += chr(((ord(c)+2) - ord('a')) % 26 + ord('a'))
    else:
        result += c
print(result)

# Expert Solution
print("Expert Solution")
result = "".join([chr(((ord(c)+2) - ord('a')) % 26 + ord('a')) if c.isalpha() else c for c in raw])
print(result)

# Solution with built-in function
print("Solution with Built-in Function")
table = str.maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")
raw.translate(table)
print(result)
