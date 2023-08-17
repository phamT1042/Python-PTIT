P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while 1:
    a = input()
    if a[0] == '0': break
    k, s = a.split()
    k, res = int(k), ""
    for i in s:
        res += P[(ord(i) - 65 + k) % 28]
    print(res[::-1])
