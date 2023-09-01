from sys import stdin, stdout, setrecursionlimit

n = int(stdin.readline())
ke = [[] for _ in range(2 * n + 1)]
color = [0] * (2 * n + 1) 
saveName, val = dict(), 1

setrecursionlimit(pow(10, 5) + 1) 
#set the maximum depth of the Python interpreter stack to the required limit. 
#This limit prevents any program from getting into infinite recursion, 
#Otherwise infinite recursion will lead to overflow of the C stack and crash the Python.
def DFS(u):
    color[u] = 1
    for v in ke[u]:
        if not color[v]:
            if DFS(v): return True
        elif color[v] == 1: return True
    color[u] = 2
    return False

def solve():
    for i in range(1, val):
        if not color[i]:
            if DFS(i): return "impossible"
    return "possible"

for _ in range(n):
    a = stdin.readline().split()
    if a[0] not in saveName: 
        saveName[a[0]] = val
        val += 1
    if a[2] not in saveName:
        saveName[a[2]] = val
        val += 1
    if a[1] == '>': ke[saveName[a[0]]].append(saveName[a[2]])
    else: ke[saveName[a[2]]].append(saveName[a[0]])

print(solve())