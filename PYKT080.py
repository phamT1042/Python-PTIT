m, n = map(int, input().split())
a, save = [], []
for i in range(m):
    a.append(list(map(int, input().split())))
    for j in range(n):
        if a[i][j] == -1: save.append([i, j])

dxy = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
res = 0
while len(save):
    i, j = save.pop(0)
    for k in dxy:
        i1, j1 = i + k[0], j + k[1]
        if i1 >= 0 and i1 < m and j1 >= 0 and j1 < n:
            res += a[i1][j1]
            a[i1][j1] = 0
print(res)

