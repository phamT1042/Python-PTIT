from sys import stdin, stdout

par = [i for i in range(100001)]
sz = [1] * 100001

def find(u):
    if u == par[u]: return u
    par[u] = find(par[u])
    return par[u]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        if sz[a] < sz[b]: a, b = b, a
        sz[a] += sz[b]
        par[b] = a

for _ in range(int(stdin.readline())):
    x, y, z = map(int, stdin.readline().split())
    if z == 1: union(x, y)
    else:
        print(1) if find(x) == find(y) else print(0)

