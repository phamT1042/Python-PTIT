from collections import deque

while 1:
    n = int(input())
    if not n: break
    save = set()
    queue = deque()
    queue.append(n)
    while len(queue):
        value = queue.popleft()
        if value == 1: break
        if value & 1:
            if (value * 3 + 1) not in save:
                save.add(value * 3 + 1)
                queue.append(value * 3 + 1)
        else:
            if (value // 2) not in save:
                save.add(value // 2)
                queue.append(value // 2)
    print(len(save) + 1)