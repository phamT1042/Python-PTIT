import sys
def stdin_gen():
    for x in sys.stdin.read().split():
        yield int(x)
cin = stdin_gen()

# import sys
# i = 0
# t = int(input())
# for line in sys.stdin:
#     n = int(line)
#     i += 1
#     if i == t: break

#for _ in range(int(sys.stdin.readline())):

#memory with array < memory with list
import sys
def stdin_gen():
    for x in sys.stdin.read().split():
        yield int(x)
cin = stdin_gen()

n = int(input())
a = []
for _ in range(n):
    a.append(next(cin))
res = pow(10, 18)

for i in range(n):
    tmp = 0
    start = a[i] - i
    last = a[i] - (n - 1 - i)
    if start > last: start, last = last, start
    if start <= 0:
        mid = a[i] + 1 - start
        tmp += 1 - start
    for j in range(i + 1, n):
        tmp += abs(mid - (j - i) - a[j])
    for j in range(i):
        tmp += abs(mid - (i - j) - a[j])
    res = min(tmp, res)
print(res)
