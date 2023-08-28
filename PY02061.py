t = int(input())
while t > 0:
    t -= 1 
    n, m = map(int, input().split())
    x, h = [], []
    for _ in range(n):
        x.append(list(map(int, input().split())))
    for _ in range(3):
        h.append(list(map(int, input().split())))

    res = 0
    for i in range(n - 2):
        for j in range(m - 2):
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    res += x[k][l] * h[k - i][l - j]
    print(res) 