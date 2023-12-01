# https://math.stackexchange.com/questions/1878810/formula-for-1k2k3k-nk-for-n-k-in-mathbbn

import math

MOD = pow(10, 9) + 7

def powMod(a, b):
    res = 1
    while b:
        if b & 1:
            res *= a
            res %= MOD
        a *= a
        a %= MOD
        b >>= 1
    return res

def inv(i): return powMod(i, MOD - 2)

for _ in range(int(input())):
    n, k = map(int, input().split())
    dp = [0] * (k + 1)
    dp[0] = n 
    for i in range(1, k + 1):
        dp[i] = (pow(n + 1, i + 1) - 1) % MOD
        for j in range(i):
            dp[i] = (dp[i] - (dp[j] * (math.comb(i + 1, j) % MOD)) % MOD + MOD) % MOD
        dp[i] = (dp[i] * inv(i + 1)) % MOD
    print(dp[k])
