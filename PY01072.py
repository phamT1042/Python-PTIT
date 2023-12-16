from sys import stdin
def stdin_gen():
    for x in stdin.read().split(): yield int(x)
cin = stdin_gen()

n, k = next(cin), next(cin)
a = set()
for i in range(n): a.add(next(cin))
a = [0] + sorted(a)
sh, n = [0] * (k + 1), len(a) - 1

def Try(i):
    for j in range(sh[i - 1] + 1, n - k + i + 1):
        sh[i] = j
        if i == k: 
            for l in range(1, k + 1): print(a[sh[l]], end = ' ')
            print()
        else: Try(i + 1)

Try(1)

