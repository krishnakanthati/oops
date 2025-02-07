a = "123456789"
res = 0
for c in a:
    d = ord(c) - ord('0')
    res = res * 10 + d
print(res)