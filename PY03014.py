t = int(input())
while t > 0:
    t -= 1
    s, stack, open = input(), [], 1
    for i in s:
        if i == '(':
            stack.append(open)
            print(open, end = ' ')
            open += 1
        elif i == ')':
            print(stack[-1], end = ' ')
            stack.pop()
    print()