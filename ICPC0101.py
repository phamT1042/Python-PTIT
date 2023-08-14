t = int(input())
a = list(map(int, input().split()))
res = []

for i in a:
    if not len(res): res.append(i)
    elif res[-1] + i & 1: res.append(i)
    else: res.pop()
print(len(res))