from sys import stdin, stdout

#Haven't submit
l = [0, 1]
for i in range(2, 26): l.append(l[-1] * 2 + 1)

def Try(n, k):
    if k == l[n] // 2 + 1: return chr(n + 64)
    if k > l[n] // 2 + 1:
        return Try(n - 1, k - l[n - 1] - 1)
    else:
        return Try(n - 1, k)

for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    stdout.write(str(Try(n, k)) + "\n")