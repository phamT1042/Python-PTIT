n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
k = int(input())

sumUp, sumDown = 0, 0
for i in range(n):
    sumUp += sum(matrix[i][: n - i - 1])
    sumDown += sum(matrix[i][n - i : n])
diff = abs(sumUp - sumDown)
print("NO", diff, sep = '\n') if diff > k else print("YES", diff, sep = '\n')