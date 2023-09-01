# import sys
# def stdin_gen():
#     for x in sys.stdin.read().split():
#         yield int(x)
# cin = stdin_gen()

# import sys
# i = 0
# t = int(input())
# for line in sys.stdin:
#     n = int(line)
#     i += 1
#     if i == t: break

#for _ in range(int(sys.stdin.readline())):

#memory with array < memory with list
n = int(input())
ke = [[] for _ in range(2 * pow(10, 5) + 1)]
color = [0] * (2 * pow(10, 5) + 1) 
saveName, saveEdge = set(), []

def value(name):
    l, r = 0, N
    while l < r:
        m = (l + r) >> 1
        if name_sort[m] == name: return m
        if name_sort[m] < name: l = m + 1
        else: r = m
    return -1

def graph():
    for n1, n2 in saveEdge:
        ke[value(n1)].append(value(n2))

def DFS(u):
    color[u] = 1
    for v in ke[u]:
        if not color[v]:
            if DFS(v): return True
        elif color[v] == 1: return True
    color[u] = 2
    return False

def solve():
    for i in range(N):
        if not color[i]:
            if DFS(i): return "impossible"
    return "possible"

for _ in range(n):
    name1, sign, name2 = input().split()
    saveName.add(name1)
    saveName.add(name2)
    if sign == '>': saveEdge.append((name1, name2))
    else: saveEdge.append((name2, name1))

name_sort = sorted(saveName)
N = len(name_sort)

graph()

print(solve())