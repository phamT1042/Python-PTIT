P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while 1:
    a = input()
    if a[0] == '0': break
    k, s = a.split()
    k, res = int(k), ""
    for i in s:
        if i == '_': i = 91
        elif i == '.': i = 92
        else: i = ord(i)
        res += P[(i - 65 + k) % 28]
    print(res[::-1])
