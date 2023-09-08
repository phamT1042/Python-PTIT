from sys import stdin, stdout
from bisect import bisect_left

for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    a = sorted(list(map(int, stdin.readline().split())))

    if n == k: stdout.write(str(a[0]) + "\n")
    else:
        pre = [0] * n
        pre[0] = a[0]
        for i in range(1, n): pre[i] = pre[i - 1] + a[i] 
        l, r = -1, pre[n - 1] // k

        def can_choose(group):
            i = bisect_left(a, group)
            return pre[i - 1] >= group * (k - n + i)

        res = -1
        while l <= r:
            m = (l + r) >> 1
            if can_choose(m): 
                res = m
                l = m + 1
            else: r = m - 1
        stdout.write(str(res) + "\n")
