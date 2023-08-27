while 1:
    n = int(input())
    if n == 0: break
    mx, mn = 0, 9e99
    for _ in range(n):
        x = int(input())
        mx = max(mx, x)
        mn = min(mn, x)
    if mx == mn: print("BANG NHAU")
    else: print(mn, mx)
