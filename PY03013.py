from functools import lru_cache
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    a -= 1
    dp_0 = [[[[-1 for _ in range(10)] for _ in range(2)] for _ in range(2)] for _ in range(10)]
    dp = [[[-1 for _ in range(10)] for _ in range(2)] for _ in range(10)]

    num = []
    while b > 0:
        num.append(b % 10)
        b //= 10
    num = num[::-1]
    val_need_cnt = 0

    @lru_cache
    def DP_0(i, lower, positive, cnt):
        if i == len(num):
            return cnt if positive else 0
        if dp_0[i][lower][positive][cnt] != -1: return dp_0[i][lower][positive][cnt]

        bound = 9 if lower else num[i]
        res = 0
        for j in range(bound + 1):
            lower2 = lower or j < bound
            positive2 = positive or j > 0
            cnt2 = cnt
            if j == 0 and positive: cnt2 += 1
            res += DP_0(i + 1, lower2, positive2, cnt2)
        
        dp_0[i][lower][positive][cnt] = res
        return res
    
    @lru_cache
    def DP(i, lower, cnt):
        if i == len(num):
            return cnt
        if dp[i][lower][cnt] != -1: return dp[i][lower][cnt]

        bound = 9 if lower else num[i]
        res = 0
        for j in range(bound + 1):
            lower2 = lower or j < bound
            cnt2 = cnt
            if j == val_need_cnt:
                cnt2 += 1
            res += DP(i + 1, lower2, cnt2)
        
        dp[i][lower][cnt] = res
        return res

    ans = [0] * 10
    ans[0] = DP_0(0, 0, 0, 0)
    dp_0 = [[[[-1 for _ in range(10)] for _ in range(2)] for _ in range(2)] for _ in range(10)]
      
    for i in range(1, 10):
        val_need_cnt = i
        ans[i] = DP(0, 0, 0)
        dp = [[[-1 for _ in range(10)] for _ in range(2)] for _ in range(10)]

    num.clear()
    if a == 0: num.append(0)
    else:
        while a > 0:
            num.append(a % 10)
            a //= 10
    num = num[::-1]

    ans[0] -= DP_0(0, 0, 0, 0)
    dp_0 = [[[[-1 for _ in range(10)] for _ in range(2)] for _ in range(2)] for _ in range(10)]
    
    for i in range(1, 10):
        val_need_cnt = i
        ans[i] -= DP(0, 0, 0)
        dp = [[[-1 for _ in range(10)] for _ in range(2)] for _ in range(10)]

    for x in ans: print(x, end = ' ')
    print()


