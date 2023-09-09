for _ in range(int(input())):
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    add = 0
    for i in map(int, input().split()):
        a[add].append(i)
        add += 1

    for i in range(n):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[pivot_row][i]): pivot_row = j
        
        if pivot_row != i:
            for j in range(i, n + 1):
                a[i][j], a[pivot_row][j] = a[pivot_row][j], a[i][j]

        for j in range(i + 1, n):
            factor = a[j][i] / a[i][i]
            for k in range(i, n + 1):
                a[j][k] -= factor * a[i][k]

    def back_substitute():
        x = [0] * (n)
        for i in range(n - 1, -1, -1):
            if not a[i][i]: return [-1]
            sum = 0
            for j in range(i + 1, n):
                sum += a[i][j] * x[j]
            x[i] = (a[i][n] - sum) / a[i][i]
        return x

    res = back_substitute()
    if len(res) == 1: print(-1)
    else:
        for x in res: print("%.3f" % x, end = ' ')
        print()