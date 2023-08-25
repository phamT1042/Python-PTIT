import sys
a = []
for line in range(int(sys.stdin.readline())):
    a.append(len(list(input().split())))

i, res, end = 0, [], 1

while i < len(a) and end:
    if a[i] == 7:
        res.append(2)
        i += 4
    elif a[i] == 6:
        res.append(1)
        while a[i] == 6: 
            if i == len(a) - 2: 
                end = 0
                break
            i += 2

sys.stdout.write(str(len(res)) + '\n')
for x in res: sys.stdout.write(str(x) + '\n')


