"""
  * http://www.pythonchallenge.com/pc/def/0.html
  * Python Challenge Level 0
"""
# power operator
print (2**38)

# power function
print(pow(2,38))

# loop
n = 1
for i in range(38):
    n *= 2
print(n)

# shift
print(1 << 38)

"""
  * http://www.pythonchallenge.com/pc/def/map.html
  * Python Challenge Level 1
"""
raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# beginner
print("Beginner Solution")
result = ""
for c in raw:
    if c.isalpha():
        result += chr(((ord(c)+2) - ord('a')) % 26 + ord('a'))
    else:
        result += c
print(result)

# advanced
print("Advance Solution")
result = "".join([chr(((ord(c)+2) - ord('a')) % 26 + ord('a')) if c.isalpha() else c for c in raw])
print(result)

# solution with built-in function
print("Solution with Built-in Function")
table = str.maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")
print(raw.translate(table))

