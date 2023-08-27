n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = dict()

for i in a:
    if i not in cnt:
        cnt[i] = 1
    else: 
        cnt[i] += 1

ordered_cnt = sorted(cnt.items(), key = lambda x: (x[1], x[0]), reverse = True) #list of tuple
if len(ordered_cnt) < 2:
    print("NONE")
else:
    i = 1
    while ordered_cnt[i][1] == ordered_cnt[0][1] and i < len(ordered_cnt) - 1: i += 1
    if ordered_cnt[i][1] == ordered_cnt[i - 1][1]: print("NONE")
    else: print(ordered_cnt[i][0])

