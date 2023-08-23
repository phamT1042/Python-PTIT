t = int(input())
while t > 0:
    t -= 1
    n, cnt, a = int(input()), dict(), []
    for i in range(n):
        x = int(input())
        a.append(x)
    a.sort()
    for x in a:
        if x not in cnt:
            cnt[x] = 1
        else: cnt[x] += 1
    sorted_cnt = sorted(cnt.items(), key = lambda x: x[1], reverse = True)
    print(sorted_cnt[0][0])