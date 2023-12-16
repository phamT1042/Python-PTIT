from collections import deque

queue = deque()
queue.append("2")
queue.append("4")
queue.append("6")
queue.append("8")
save = []

while len(queue):
    tmp = queue.popleft()
    save.append(tmp + tmp[::-1])
    if len(tmp) == 3: continue
    queue.append(tmp + "0")
    queue.append(tmp + "2")
    queue.append(tmp + "4")
    queue.append(tmp + "6")
    queue.append(tmp + "8")

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in save:
        if int(i) >= n: break
        print(i, end = ' ')
    print()
