from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    bit = []
    dis = b - a + 1

    while b > 0:
        bit.append(b % 2)
        b //= 2
    bit = bit[::-1]
    n = len(bit)

    dp = [[[[[-1 for i in range(n + 1)] for _ in range(n + 1)] for j in range(2)] for k in range(2)] for h in range(n + 1)]

    def DP(i, lower, positive, length, cnt1):
        if i == n:
            return cnt1 / (length + 1) if length else 0
        if dp[i][lower][positive][length][cnt1] != -1: return dp[i][lower][positive][length][cnt1]

        bound = 1 if lower else bit[i]
        res = 0
        for j in range(bound + 1):
            lower2 = lower or j < bound
            positive2 = positive or j == 1
            length2 = length
            if positive: length2 += 1
            cnt1_new = cnt1
            if j == 1: cnt1_new += 1
            res += DP(i + 1, lower2, positive2, length2, cnt1_new)

        dp[i][lower][positive][length][cnt1] = res
        return res
    
    rangeR = DP(0, 0, 0, 0, 0)
    rangeL = 0

    if a > 1:
        a -= 1
        bit.clear()
        while a > 0:
            bit.append(a % 2)
            a //= 2
        bit = bit[::-1]
        n = len(bit)

        dp = [[[[[-1 for i in range(n + 1)] for _ in range(n + 1)] for j in range(2)] for k in range(2)] for h in range(n + 1)]
        rangeL += DP(0, 0, 0, 0, 0)
    
    stdout.write("%.5f\n" % ((rangeR - rangeL) / dis))