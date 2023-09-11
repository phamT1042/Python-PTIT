from collections import deque

n = int(input())
s = deque()
s.append([int(input()), 1])
res = 0
for i in range(1, n):
    x = int(input())
    while len(s) > 0:
        if x < s[-1][0]:
            res += 1
            s.append([x, 1])
            break
        else:
            tmp = s.pop()
            res += tmp[1]
            if tmp[0] == x:
                res += 1 if len(s) > 0 else 0
                s.append([x, tmp[1] + 1])
                break
    if len(s) == 0:
        s.append([x, 1])
print(res)

