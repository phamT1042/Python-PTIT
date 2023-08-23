t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    res = [1] * n
    stack = [0]
    for i in range(1, n):
        while a[i] > a[stack[-1]]:
            res[i] += res[stack[-1]]
            stack.pop()
            if not len(stack): break
        stack.append(i)
    for x in res: print(x, end = ' ')
    print()