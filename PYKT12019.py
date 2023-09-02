t = int(input())
while t > 0:
    t -= 1
    n, a = int(input()), list(map(int, input().split()))
    a.insert(0, -1)
    a.append(pow(10, 9))

    pre, suff = [-1] * (n + 2), [pow(10, 9)] * (n + 2)
    for i in range(1, n + 1):
        pre[i] = max(pre[i - 1], a[i])
    for i in range(n, 0, -1):
        suff[i] = min(suff[i + 1], a[i])

    res = 0
    for i in range(1, n + 1):
        if a[i] >= pre[i - 1] and a[i] < suff[i + 1]: res += 1
    print(res)
    
        
