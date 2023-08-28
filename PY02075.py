t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    edge = []
    for _ in range(n):
        edge.append(list(map(int, input().split())))
    
    edge.sort(key = lambda x: x[1])
    res, end = 1, edge[0][1]
    for i in range(1, n):
        if edge[i][0] >= end:
            end = edge[i][1]
            res += 1
    print(res)