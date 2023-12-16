from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
can_not_solve = sum(a)

def calcSum(h):
    sm = 0
    for i in range(n):
        flag = 0
        l, r, res = 1, a[i], a[i]
        while l <= r:
            m = (l + r) >> 1
            if a[i] // m == h:
                flag, res, r = 1, m, m - 1
            elif a[i] // m < h: r = m - 1 
            else:
                l = m + 1
        if flag == 0: return can_not_solve
        sm += res
    return sm
            
mx = min(a)
res = can_not_solve
for i in range(2, mx + 1):
    res = min(res, calcSum(i))

print(res)
