from math import gcd
from sys import stdin, stdout
def stdin_gen():
    for x in stdin.read().split():
        yield int(x)
cin = stdin_gen()

t = next(cin)
while t > 0:
    t -= 1
    n, k = next(cin), next(cin)
    a = []
    for _ in range(n):
        a.append(next(cin))
    res = 1001
    for i in range(0, n):
        g = a[i]
        for j in range(i, n):
            g = gcd(a[j], g)
            if g == k: 
                res = min(res, j - i + 1)
                break
    stdout.write(str(res) + "\n") if res != 1001 else stdout.write("-1\n")