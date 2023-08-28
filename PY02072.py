n = int(input())
a = list(map(int, input().split()))
tmp, res, mx = 0, 0, max(a)
for i in a:
    if i == mx:
        tmp += 1
    else:
        res = max(res, tmp)
        tmp = 0
print(max(res, tmp))