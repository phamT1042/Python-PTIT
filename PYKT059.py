n, m, u = map(int, input().split())
ke = [[] for i in range(n + 1)]

for _ in range(m):
    data = input().split()
    ke[int(data[0])].append(int(data[1]))
    ke[int(data[1])].append(int(data[0]))

vs = [0] * (n + 1)
def DFS(x):
    vs[x] = 1
    for v in ke[x]:
        if not vs[v]: DFS(v)

DFS(u)
for i in range(1, n + 1):
    if not vs[i]: print(i)