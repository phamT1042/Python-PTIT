from sys import stdin, stdout

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
can_not_solve = sum(a)

def calcSum(h):
    b = a.copy()
    for i in range(n):
        flag = 0
        for j in range(1, b[i]):
            if b[i] // j == h:
                flag = 1
                b[i] = j
                break
        if flag == 0: return can_not_solve
    return int(sum(b))
            

mx = min(a)
res = can_not_solve
for i in range(2, mx + 1):
    res = min(res, calcSum(i))

print(res)