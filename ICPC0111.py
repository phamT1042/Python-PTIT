t = int(input())

while t > 0:
    t -= 1
    n, d = map(int, input().split())
    a = list(input().split())
    d %= n
    for i in range(d, n): print(a[i], end = ' ')
    for i in range(0, d): print(a[i], end = ' ')
    print()
