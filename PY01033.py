import math

l, r = map(int, input().split())
for i in range(l, r - 1):
    for j in range(i + 1, r):
        if math.gcd(i, j) == 1:
            for k in range(j + 1, r + 1):
                if math.gcd(k, j) == math.gcd(i, k) == 1:
                    print("({0}, {1}, {2})".format(i, j, k))
            