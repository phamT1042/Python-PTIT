from sys import stdin, stdout
from math import ceil, log2

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    res = 0
    for i in range(1, n):
        mn = min(a[i], a[i - 1])
        mx = max(a[i], a[i - 1])     
        if mn != mx:
            res += ceil(log2(mx / mn) - 1)
    
    stdout.write(str(res) + '\n')