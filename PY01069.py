from collections import deque
from sys import stdin, stdout

n = int(stdin.readline())
q = deque()
q.append(['2', 1, 0, 0, 0])
q.append(['3', 0, 1, 0, 0])
q.append(['5', 0, 0, 1, 0])
q.append(['7', 0, 0, 0, 1])
while len(q):
    tmp = q.popleft()
    if len(tmp) == 1:  
        if tmp[0][-1] != '2':
            stdout.write(str(tmp[0]) + "\n")
        if len(tmp[0]) < n:
            q.append([tmp[0] + '2'])
            q.append([tmp[0] + '3'])
            q.append([tmp[0] + '5'])
            q.append([tmp[0] + '7'])
    else:
        if tmp[0][-1] != '2' and tmp[1] > 0 and tmp[2] > 0 and tmp[3] > 0 and tmp[4] > 0:
            stdout.write(str(tmp[0]) + "\n")
        if len(tmp[0]) < n:
            q.append([tmp[0] + '2', tmp[1] + 1, tmp[2], tmp[3], tmp[4]])
            q.append([tmp[0] + '3', tmp[1], tmp[2] + 1, tmp[3], tmp[4]])
            q.append([tmp[0] + '5', tmp[1], tmp[2], tmp[3] + 1, tmp[4]])
            q.append([tmp[0] + '7', tmp[1], tmp[2], tmp[3], tmp[4] + 1])
