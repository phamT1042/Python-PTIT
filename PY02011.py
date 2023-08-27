n = int(input())
a = list(map(int, input().split()))

pair = []
for i in range(n): pair.append([a[i], i])
pair.sort(key = lambda x: x[0])

if n & 1:
    m, tmp = n // 2, 0
    for i in range(n):
        tmp += abs(pair[i][0] - pair[m][0])
    print(tmp, pair[m][0])
else:
    tmp1, tmp2, m1, m2 = 0, 0, n // 2 - 1, n // 2
    for i in range(n):
        tmp1 += abs(pair[i][0] - pair[m1][0])
        tmp2 += abs(pair[i][0] - pair[m2][0])
    if tmp1 == tmp2:
        print(tmp2, pair[m2][0]) if pair[m2][1] < pair[m1][1] else print(tmp1, pair[m1][0])
    else:
        print(tmp2, pair[m2][0]) if tmp2 < tmp1 else print(tmp1, pair[m1][0])
    
