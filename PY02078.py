t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a, b = [0] * n, [0] * n
    for i in range(n):
        a[i], b[i] = map(float, input().split())

    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and b[i] < b[j]: dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))