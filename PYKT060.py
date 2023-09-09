# Kiểm tra các thành phần liên thông đều đầy đủ là được

n, m = int(input()), int(input())
ke = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    ke[x].append(y)
    ke[y].append(x)

vs = [0] * (n + 1)
sub = []

def DFS(u):
    vs[u] = 1
    sub.append(u)
    for v in ke[u]:
        if not vs[v]: DFS(v)

def solve():
    for i in range(1, n + 1):
        if not vs[i]:
            sub.clear()
            DFS(i)
            if len(sub) > 1:
                for j in sub:
                    if len(ke[j]) != len(sub) - 1: return "NO"
    return "YES"

print(solve())