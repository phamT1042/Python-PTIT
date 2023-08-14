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
    cnt = 0
    for i in prime:
        if i > n - 6: break
        if sang[i + 2] and sang[i + 6] or sang[i + 4] and sang[i + 6]: cnt += 1
    print(cnt)

    
