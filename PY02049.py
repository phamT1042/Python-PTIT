t = int(input())
while t > 0:
    t -= 1
    n, p = map(int, input().split())
    res = 0
    for i in range(2, n + 1):
        while i % p == 0:
            i //= p
            res += 1
    print(res)
