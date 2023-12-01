n = int(input())
a = list(map(int, input().split()))
res = pow(10, 18)

for i in range(n):
    b = a.copy()
    change = 0
    for j in range(i):
        b[j] += change
        change -= 1
    for j in range(i, n):
        b[j] += change
        change += 1
    
    b.sort()
    start = max(-change, b[n // 2], 0)
    step = 0
    
    for j in range(i):
        step += abs(start - a[j])
        start += 1
    for j in range(i, n):
        step += abs(start - a[j])
        start -= 1
    res = min(res, step)
print(res)