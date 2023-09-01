#memory with array < memory with list
t = int(input())
while t > 0:
    t -= 1
    n, c, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse = True)

    if c > d: c, d = d, c
    print("%.6f" % ((sum(a[:c]) / c + sum(a[c:c + d]) / d)))