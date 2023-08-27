#row 0: (n - 1)A0 + A1 + A2 + ... + An = sum(row0)
#row 1: A0 + (n - 1)A1 + A2 + ... + An = sum(row1)
#=> (n - 2)A0 + (2 - n)A1 = sum(row0) - sum(row1) and A0 + A1 = B[0][1]
#=> A0 = (sum(row0) - sum(row1) - (2 - n)B[0][1]) / 2(n - 2)

n = int(input())
a = [0 for i in range(n)]

b = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    b.append(tmp)

if n == 1: print(b[0][0])
elif n == 2:
    print(1, b[0][1] - 1)
else:
    sum_row_0, sum_row_1 = sum(b[0]), sum(b[1])
    a[0] = (sum_row_0 - sum_row_1 - (2 - n) * b[0][1]) // (2 * (n - 2))
    for i in range(1, n):
        a[i] = b[0][i] - a[0]
    for x in a: print(x, end = ' ')
