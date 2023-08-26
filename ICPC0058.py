#1 đỉnh thắt x của 1 cặp đỉnh (u, v) là đỉnh mà tất cả đường đi từ u tới v đều phải đi qua nó.
#<=> Mọi đường đi từ u nếu không đi qua x sẽ không đến được v

from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n, m, u, v = map(int, stdin.readline().split())
    ke = [[] for i in range(n + 1)]
    for _ in range(m):
        x, y = map(int, stdin.readline().split())
        ke[x].append(y)

    def BFS(skip):
        vs = [0 for i in range(n + 1)]
        queue = [u]
        vs[u], vs[skip] = 1, 1
        while len(queue):
            tmp = queue.pop(0)
            if tmp == v: return False
            for i in ke[tmp]:
                if not vs[i]:
                    queue.append(i)
                    vs[i] = 1
        return True

    res = 0
    for i in range(1, n + 1):
        if i == u or i == v: continue
        if BFS(i): res += 1
    print(res)