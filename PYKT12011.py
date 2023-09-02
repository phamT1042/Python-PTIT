from sys import stdin, stdout
from math import gcd

for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    s = stdin.readline()

    cnt1 = [0] * (n + 1) 
    for i in range(1, n + 1):
        cnt1[i] = cnt1[i - 1] + (s[i - 1] == '1')
    
    m, t = n * n, 0 
    for i in range(1, n + 1):
        if s[i - 1] == '1':
            if i <= k: t += 1 + 2 * (cnt1[i] - 1) 
            else: t += 1 + 2 * ((cnt1[i] - cnt1[i - k - 1]) - 1)
    
    tg = gcd(t, m)
    print("{0}/{1}".format(t // tg, m // tg))