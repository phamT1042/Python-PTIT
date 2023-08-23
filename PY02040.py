n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
k = int(input())

sumUp, sumDown = 0, 0
for i in range(n):
    for j in range(n - i - 1): sumUp += matrix[i][j]
    for j in range(n - i, n): sumDown += matrix[i][j]
diff = abs(sumUp - sumDown)
print("NO", diff, sep = '\n') if diff > k else print("YES", diff, sep = '\n')