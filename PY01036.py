t = int(input())
while t > 0:
    t -= 1
    n, res = int(input()), 0
    st = 1 if n & 1 else 2
    for i in range(st, n + 1, 2): res += 1 / i
    print("%.6f" % res)
