n, k = map(int, input().split())
before = list(map(int, input().split()))
after = list(map(int, input().split()))
save = [[] for _ in range(n)]

for i in range(n):
    save[i] = [before[i], after[i]]

save.sort(key = lambda x: (x[0] - x[1]))
i, res = 0, 0
while i < n:
    if k: 
        res += save[i][0]
        k -= 1
    else:
        if save[i][0] < save[i][1]: res += save[i][0]
        else: res += save[i][1]
    i += 1
print(res)