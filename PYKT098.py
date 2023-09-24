f = open("DATA.in", "r")
lines = f.readlines()
f.close()
res = []
for line in lines:
    check = line.split()
    for a in check:
        try: 
            num = int(a)
            if num > 2147483647 or num < -2147483648: res.append(num)
        except: 
            res.append(a)

for x in sorted(res, key = str): print(x, end = ' ')