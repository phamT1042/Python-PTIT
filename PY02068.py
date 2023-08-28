from sys import stdin, stdout

t = int(stdin.readline())
while t > 0:
    t -= 1 
    n, m, r = map(int, stdin.readline().split())
    x = [[0] * (m + 1)] * (n + 1)
    for i in range(1, n + 1):
        x[i] = [0] + list(map(int, stdin.readline().split()))

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x[i][j] += x[i - 1][j] + x[i][j - 1] - x[i - 1][j - 1]

    for i in range(r, n + 1):
        for j in range(r, m + 1):
            stdout.write(str(int((x[i][j] - x[i - r][j] - x[i][j - r] + x[i - r][j - r]) / pow(r, 2))) + " ")
        stdout.write("\n")