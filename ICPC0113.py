sang = [1 for _ in range(1000000)]
sang[0] = sang[1] = 0
for i in range(2, 1000):
    if sang[i]:
        for j in range(i * i, 1000000, i):
            sang[j] = 0

prime = []
for i in range(1000000):
    if sang[i]: prime.append(i)

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    used = [1 for _ in range(1000000)]
    for i in prime:
        if i >= n: break
        reverse = int(str(i)[::-1])
        if sang[reverse] and i != reverse and used[i] and used[reverse] and reverse < n:
            print(i, reverse, end = ' ')
            used[i] = used[reverse] = 0
    print()

    
