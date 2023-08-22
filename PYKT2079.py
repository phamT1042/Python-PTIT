import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    num = []
    while n > 0:
        num.append(n % 10)
        n //= 10
    num = num[::-1]
    mx = len(num)

    dp = [[[[-1 for i in range(8)] for k in range(mx + 1)] for h in range(2)] for _ in range(mx + 1)]
    
    def DP(i, lower, cnt68, mod8):
        if i == mx:
            return cnt68 if not mod8 else 0
        if dp[i][lower][cnt68][mod8] != -1: return dp[i][lower][cnt68][mod8]

        bound = 9 if lower else num[i]

        res = 0
        for j in range(bound + 1):
            lower2 = lower or j < bound
            mod8_new = ((mod8 * 2) % 8 + (j % 8)) % 8
            cnt68_new = cnt68
            if j == 6 or j == 8: cnt68_new += 1
            res += DP(i + 1, lower2, cnt68_new, mod8_new)

        dp[i][lower][cnt68][mod8] = res
        return dp[i][lower][cnt68][mod8]
   
    print(DP(0, 0, 0, 0))