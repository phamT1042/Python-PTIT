# Các số có dạng phân tích a1^d1 . a2^d2 . ....
# Số có 9 ước <=> (d1+1)(d2+1)...(dn+1) = 1*9 = 3*3
# => TH1: nếu a là prime => a ^ 8 là số có 9 ước
# => TH2: nếu a là số 9 ước => a = a1^2 * a2^2 => sqrt(a) = a1 * a2 với a1 != a2 và (a1, a2) != 1 
from math import sqrt

n = int(input())
m = int(sqrt(n))
sang = [i for i in range(m + 1)]
for i in range(2, int(sqrt(m)) + 1):
    if sang[i] == i:
        for j in range(i * i, m + 1, i):
            sang[j] = i

res = 0
for i in range(2, m + 1):
    a1 = sang[i]
    a2 = sang[i // sang[i]]
    if a1 * a2 == i and a2 != 1 and a1 != a2: 
        res += 1
    elif sang[i] == i:
        if i ** 8 <= n: res += 1
print(res)