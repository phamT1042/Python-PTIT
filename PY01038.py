t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if not n % 7: print(n)
    else:
        cnt = 0
        while n % 7:
            n = n + int(str(n)[::-1])
            cnt += 1
            if cnt == 1000: break
        print(-1) if n % 7 else print(n)

