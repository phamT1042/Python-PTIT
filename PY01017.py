t = int(input())
while t > 0: 
    t -= 1
    s, res = input(), ""
    cnt = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            res += str(cnt) + s[i - 1]
            cnt = 1
        else:
            cnt += 1
    res += str(cnt) + s[len(s) - 1]
    print(res)

