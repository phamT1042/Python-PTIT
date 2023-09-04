import sys
sys.setrecursionlimit(5000)

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    dp = [[-1 for _ in range(5 * k)] for _ in range(n)]

    def DP(i, cnt):
        if i == n or cnt == 5 * k:
            return 0
        if dp[i][cnt] != -1:
            return dp[i][cnt]
        
        factor = cnt % 5 + 1
        if factor % 2 == 0:
            factor = -factor
        res = a[i] * factor + DP(i + 1, cnt + 1)

        if 5 * k - cnt < n - i:
            res = max(res, DP(i + 1, cnt))

        dp[i][cnt] = res
        return res
    
    print(DP(0, 0))
