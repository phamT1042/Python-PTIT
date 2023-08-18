t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    res, start = 0, 1
    start = 1 if n & 1 else 2
    for i in range(start, n + 1, 2): res += 1 / i
    print(f"%.6f" % res)
    