from collections import deque

n = int(input())

q = deque()
q.append(('A', 1, 0, 0))
q.append(('B', 0, 1, 0))
q.append(('C', 0, 0, 1))

while len(q):
    tmp = q.popleft()
    if tmp[1] and tmp[2] and tmp[3] and tmp[3] >= tmp[2] >= tmp[1]: print(tmp[0])

    if len(tmp[0]) < n:
        q.append((tmp[0] + 'A', tmp[1] + 1, tmp[2], tmp[3]))
        q.append((tmp[0] + 'B', tmp[1], tmp[2] + 1, tmp[3]))
        q.append((tmp[0] + 'C', tmp[1], tmp[2], tmp[3] + 1))
