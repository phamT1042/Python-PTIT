from collections import deque

for _ in range(int(input())):
    n = int(input())
    q = deque()
    for i in range(2, 9, 2): q.append(str(i))

    while 1:
        tmp = q.popleft()
        if int(tmp + tmp[::-1]) >= n: break
        print(tmp + tmp[::-1], end = ' ')

        for i in range(0, 9, 2): q.append(tmp + str(i))
    print()
