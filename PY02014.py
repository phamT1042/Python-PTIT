from bisect import bisect_left

sang = [1 for i in range(10008)]
prime = []
sang[0] = sang[1] = 0
for i in range(2, 101):
    if sang[i]:
        for j in range(i * i, 10008, i): sang[j] = 0
for i in range(2, 10008):
    if sang[i]:
        prime.append(i)

n = int(input())
a = list(map(int, input().split()))
res = 0
for i in a:
    if sang[i] == 0:
        if i < 2: res = max(res, 2 - i)
        else:
            pos = bisect_left(prime, i)
            res = max(res, min(prime[pos] - i, i - prime[pos - 1]))
print(res)