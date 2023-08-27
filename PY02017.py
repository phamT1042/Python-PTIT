t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    res = a[0]
    for i in range(1, n): res ^= a[i]
    print(res)