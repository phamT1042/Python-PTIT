from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    res = 0
    for i in range(1, n):
        mn = min(a[i], a[i - 1])
        mx = max(a[i], a[i - 1])
        while mx > 2 * mn:
            res += 1
            mn *= 2
    print(res)



