n, i = input(), 0
res = ""
if len(n) % 3:
    i += len(n) % 3
    res += n[:i]
    for j in range(i, len(n), 3):
        res += "," + n[j:j + 3]
else:
    for j in range(0, len(n), 3):
        res += n[j:j + 3]
        if j < len(n) - 3: res += ","
print(res)