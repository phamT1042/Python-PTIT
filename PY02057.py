n, m = map(int, input().split())
a, saveMax, saveMin = [], 0, 10001

for _ in range(n):
    b = list(map(int, input().split()))
    saveMax = max(saveMax, max(b))
    saveMin = min(saveMin, min(b))
    a.append(b)

mm, res = saveMax - saveMin, []

for i in range(n):
    for j in range(m):
        if a[i][j] == mm: res.append((i, j))

if len(res):
    print(mm)
    for i in res:
        print("Vi tri [%d][%d]" % (i[0], i[1]))
else:
    print("NOT FOUND")