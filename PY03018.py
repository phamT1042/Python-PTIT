from sys import stdin, stdout
from collections import deque

a = [[]] * 1000
for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    for i in range(n): a[i] = list(map(int, input().split()))

    def BFS():
        queue = deque()
        queue.append((0, 0, 0))
        vs = [[0 for i in range(m)] for j in range(n)]
        vs[0][0] = 1
        while len(queue):
            i, j, steps = queue.popleft()
            if i == n - 1 and j == m - 1: return steps
            for k in range(3):
                if k == 0 and i < n - 1:
                    go = abs(a[i][j] - a[i + 1][j])
                    if i + go < n: 
                        if not vs[i + go][j]:
                            queue.append((i + go, j, steps + 1))
                            vs[i + go][j] = 1

                elif k == 1 and j < m - 1:
                    go = abs(a[i][j] - a[i][j + 1])
                    if j + go < m: 
                        if not vs[i][j + go]:
                            queue.append((i, j + go, steps + 1))
                            vs[i][j + go] = 1

                elif i < n - 1 and j < m - 1:
                    go = abs(a[i][j] - a[i + 1][j + 1])
                    if j + go < m and i + go < n: 
                        if not vs[i + go][j + go]:
                            queue.append((i + go, j + go, steps + 1))
                            vs[i + go][j + go] = 1
        return -1

    stdout.write(str(BFS()) + "\n")
