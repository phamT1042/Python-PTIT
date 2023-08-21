t = int(input())
while t > 0:
    t -= 1
    n, k = map(int, input().split())
    tmp = n

    num = []
    while n > 0:
        num.append(n % 2)
        n //= 2
    num = num[::-1]

    dp = [[[[-1 for i in range(2)] for j in range(len(num))] for k in range(2)] for h in range(len(num))]
    
    def DP(i, lower, cnt, positive):
        if i == len(num):
            return 1 if cnt == k and positive else 0
        if dp[i][lower][cnt][positive] != -1: return dp[i][lower][cnt][positive]

        bound = 1 if lower else num[i]

        res = 0
        for j in range(bound + 1):
            lower2 = lower or j < num[i]
            positive2 = positive or j == 1
            cnt2 = cnt
            if positive:
                if j == 0: cnt2 += 1
            res += DP(i + 1, lower2, cnt2, positive2)

        dp[i][lower][cnt][positive] = res
        return dp[i][lower][cnt][positive]
   
    print(DP(0, 0, 0, 0) + (k == 1))

