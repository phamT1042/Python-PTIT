t = int(input())
while t > 0:
    t -= 1
    s = input()
    if len(s) > 100:
        i = 99
        while s[i] != ' ': i -= 1
        print(s[:i + 1])
    else:
        print(s)