sang = [1] * 136
sang[0] = sang[1] = 0
for i in range(2, 13):
    if sang[i]:
        for j in range(i * i, 136, i): sang[j] = 0

n = int(input())

num = []
while n > 0:
    num.append(n % 10)
    n //= 10
num = num[::-1]
mx = len(num)

dp = [[[[-1 for k in range(136)] for j in range(136)] for i in range(3)] for _ in range(mx + 1)]
    
def DP(i, carry, sumX, sumY):
    if i == -1:
        return 1 if not carry and sang[sumX] and sang[sumY] else 0
    if dp[i][carry][sumX][sumY] != -1: return dp[i][carry][sumX][sumY]

    res = 0
    for j in range(10):
        for k in range(10):
            if (j + 2 * k + carry) % 10 == num[i]:
                res += DP(i - 1, (j + 2 * k + carry) // 10, sumX + j, sumY + k)

    dp[i][carry][sumX][sumY] = res
    return dp[i][carry][sumX][sumY]
   
print(DP(mx - 1, 0, 0, 0))