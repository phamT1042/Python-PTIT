import math
t = int(input())
while t > 0:
    t -= 1
    n, x, m = map(float, input().split())
    print(math.ceil(math.log(m / n, 1 + x / 100)))
