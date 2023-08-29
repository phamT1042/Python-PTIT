#N = (x + 0) + (x + 1) + (x + 2) + ... + (x + n)
#N = (n + 1)x + n(n+1)/2 => x = (N - n(n+1)/2)/(n+1)

t = int(input())
while t > 0:
    t -= 1
    N = int(input())
    res, n = 0, 1
    while 1:
        tu = N - (n * (n + 1)) // 2
        if tu <= 0: break
        res += 1 if ((tu / (n + 1)) == tu // (n + 1)) else 0
        n += 1
    print(res)