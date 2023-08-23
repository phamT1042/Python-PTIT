t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    res = [1] * n
    stack = [[a[0], 0]]
    for i in range(1, n):
        while a[i] > stack[-1][0]:
            res[i] += res[stack[-1][1]]
            stack.pop()
            if not len(stack): break
        stack.append([a[i], i])
    for x in res: print(x, end = ' ')
    print()