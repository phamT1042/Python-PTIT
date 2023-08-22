from bisect import bisect_left

hamming = []
mx = 10**18
for i in range(61):
    for j in range(39):
        a = 2**i * 3**j
        if a > mx: break
        for k in range(27):
            b = a * 5**k
            if b > mx: break
            hamming.append(b)
hamming.sort()

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    index = bisect_left(hamming, n)
    print(index + 1) if index != len(hamming) and hamming[index] == n else print("Not in sequence")


