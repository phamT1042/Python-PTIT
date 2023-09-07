n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))

if k == 1: print(0)
else:
    MOD = pow(10, 9) + 7
    f = [1]
    for i in range(1, n + 1): f.append((f[i - 1] * i) % MOD)

    def powM(a, b):
        res = 1
        while b:
            if b & 1: 
                res = (res * a) % MOD
            a = (a * a) % MOD
            b //= 2
        return res

    def C(n, k):
        return (f[n] * powM((f[n - k] * f[k]) % MOD, MOD - 2)) % MOD

    res, diff = 0, 0
    for i in range(n - k + 1):
        diff = (diff + a[n - i - 1] - a[i]) % MOD
        res = (res + (diff * C(n - i - 2, k - 2)) % MOD) % MOD
    print(res)






