for _ in range(int(input())):
    n, m, u, v = map(int, input().split())
    ke = [[] for i in range(n + 1)]
    for i in range(m):
        s, e = map(int, input().split())
        ke[s].append(e)

    res = 0
    for i in range(1, n + 1):
        if i == u or i == v: continue
        vs = [0] * (n + 1)
        vs[u], vs[i] = 1, 1

        def DFS(i):
            vs[i] = 1
            for j in ke[i]:
                if not vs[j]: DFS(j)
        
        DFS(u)
        if not vs[v]: res += 1
    print(res)