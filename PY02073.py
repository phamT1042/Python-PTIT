t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    x, y, z = map(int, input().split())
    dp = [0] * (n + 1)
    dp[1] = x
    for i in range(2, n + 1):
        if i & 1:
            dp[i] = min(dp[i - 1] + x, dp[(i + 1) // 2] + y + z)
        else:
            dp[i] = min(dp[i - 1] + x, dp[i // 2] + z)
    print(dp[n])