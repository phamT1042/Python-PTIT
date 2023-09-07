# A + A^2 = A(I + A)
# A + A^2 + A^3 = A(I + A) + A^3
# A + A^2 + A^3 + A^4 = (A + A^2)(I + A^2) = A(I + A)(I + A^2)

# B(k) = A + ... + A^k
# B(1) = A
# B(k) = B(k / 2) * (I + A^(k / 2)) if k is even
# B(k) = B(k / 2) * (I + A^(k / 2)) + A^k if k is odd
from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
A = [[] * n for j in range(n)]
I = [[0] * n for j in range(n)]
T = [[0] * n for j in range(n)]
for i in range(n):
    I[i][i] = 1
    A[i] = list(map(int, stdin.readline().split()))
    for j in range(n): A[i][j] %= 10

def add(X, Y):
    Z = [i.copy() for i in T]
    for i in range(n):
        for j in range(n):
            Z[i][j] = (X[i][j] + Y[i][j]) % 10
    return Z

def mul(X, Y):
    Z = [i.copy() for i in T]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i][j] = (Z[i][j] + X[i][k] * Y[k][j]) % 10
    return Z

def powM(X, power):
    Z = [i.copy() for i in I]
    while power:
        if power & 1:
            Z = mul(Z, X)
        X = mul(X, X)
        power >>= 1
    return Z

def solve(A, k):
    if k == 0: return I
    if k == 1: return A
    if k & 1:
        return add(mul(solve(A, k >> 1), add(I, powM(A, k >> 1))), powM(A, k))
    else:
        return mul(solve(A, k >> 1), add(I, powM(A, k >> 1)))

B = solve(A, k)
for i in B:
    for j in i: stdout.write(str(j) + " ")
    stdout.write("\n")