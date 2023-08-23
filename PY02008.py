from math import sqrt

mx = 8000
sang = [1] * mx
sang[0] = sang[1] = 0
for i in range(2, int(sqrt(mx)) + 1):
    if sang[i]:
        for j in range(i * i, mx, i): sang[j] = 0
    
prime = [0]
for i in range(mx): 
    if sang[i]: prime.append(i)

n, x = map(int, input().split())
for i in range(n + 1):
    x += prime[i]
    print(x, end = ' ')
