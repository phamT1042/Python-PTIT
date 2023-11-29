t = int(input())
while t > 0:
    t -= 1
    s = input()
    l, r, res = 0, len(s) - 1, "YES"
    while l < r:
        if abs(ord(s[l]) - ord(s[l + 1])) != abs(ord(s[r]) - ord(s[r - 1])):
            res = "NO"
            break
        l += 1
        r -= 1
    print(res)

