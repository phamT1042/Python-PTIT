t = int(input())
while t > 0:
    t -= 1
    s = input()
    res, i, n = 1e19, 0, len(s)
    while i < n:
        if '0' <= s[i] <= '9':
            pos = i
            while i < n and '0' <= s[i] <= '9':
                i += 1
            res = min(res, int(s[pos:i]))
        i += 1
    print(res)
