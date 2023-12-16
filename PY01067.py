from sys import stdin, stdout
from collections import deque

save, q = set(), deque()
q.append(('1', 0))
q.append(('2', 1))

while len(save) <= 1000:
    tmp = q.popleft()
    cur_str, cnt2 = tmp[0], tmp[1]
    if cnt2 > (len(cur_str) // 2):
        save.add(cur_str)
    for i in range(0, 3):
        if i == 2:
            q.append([cur_str + str(i), cnt2 + 1])
        else:
            q.append([cur_str + str(i), cnt2]) 

save_sort = sorted(save, key = int)

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    for i in range(n): stdout.write(str(save_sort[i]) + " ")
    stdout.write("\n")
