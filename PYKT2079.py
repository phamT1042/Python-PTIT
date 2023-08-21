t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    tmp = n

    num = []
    while n > 0:
        num.append(n % 10)
        n //= 10
    num = num[::-1]

    dp = [[[[-1 for i in range(8)] for k in range(36)] for h in range(2)] for _ in range(len(num))]
    
    def DP(i, lower, cnt68, mod8):
        if i == len(num):
            return cnt68 if not mod8 else 0
        if dp[i][lower][cnt68][mod8] != -1: return dp[i][lower][cnt68][mod8]

        bound = 9 if lower else num[i]

        res = 0
        for j in range(bound + 1):
            lower2 = lower or j < bound
            mod8_new = ((mod8 * 2) % 8 + j % 8) % 8
            cnt68_new = cnt68
            if j == 6 or j == 8: cnt68_new += 1
            res += DP(i + 1, lower2, cnt68_new, mod8_new)

        dp[i][lower][cnt68][mod8_new] = res
        return dp[i][lower][cnt68][mod8_new]
   
    print(DP(0, 0, 0, 0))

