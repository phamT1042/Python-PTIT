t = int(input())
while t > 0:
    t -= 1
    s = input()
    n = len(s)
    if n < 3: print("NO")
    else:
        l, r = 0, n - 1
        while s[l + 1] > s[l]: l += 1
        while s[r - 1] > s[r]: r -= 1
        print("YES") if l == r else print("NO")