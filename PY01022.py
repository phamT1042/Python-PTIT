n = input()
res = 0

#tính cả giá trị của dấu âm ?
while len(n) > 1:
    n = str(sum([ord(x) - ord('0') for x in n]))
    res += 1
print(res)