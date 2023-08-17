a, k, n = map(int, input().split())
check = 0

i = 1
while 1:
    if k * i > n: break
    if k * i - a > 0: 
        print(k * i - a, end = ' ')
        check = 1
    i += 1
if not check: print(-1)