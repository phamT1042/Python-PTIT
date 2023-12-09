mod = pow(10, 9) + 7
n, m, k = map(int, input().split())

saveR, saveC = dict(), dict()
while k > 0:
    k -= 1
    t, x, y = input().split()
    x, y = int(x), int(y)
    if t == 'S':
        try: saveC[x] *= y
        except: saveC[x] = y
        saveC[x] %= mod 
    else:
        try: saveR[x] *= y
        except: saveR[x] = y
        saveR[x] %= mod 

#a[i][j] = m * (i - 1) + j (1 <= i <= n; 1 <= j <= m)
# => sum_row[i] = ((2 * m * i - m + 1) * m) // 2
# => sum_column[j] = ((2 * j + m * n - m) * n) // 2
res = ((m * n + 1) * (m * n)) // 2
res %= mod

for i in saveR.keys():
    res += (((2 * m * i - m + 1) * m) // 2) * (saveR[i] - 1)
    res %= mod

for j in saveC.keys():
    res += (((2 * j + m * n - m) * n) // 2) * (saveC[j] - 1)
    res %= mod

for i in saveR.keys():
    for j in saveC.keys():
        aij = (m * (i - 1) + j) % mod
        res += aij * saveR[i] * saveC[j] - aij * (saveR[i] + saveC[j] - 1)
        res = (res + mod) % mod
print(res)





