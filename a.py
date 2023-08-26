# import sys
# def stdin_gen():
#     for x in sys.stdin.read().split():
#         yield int(x)
# cin = stdin_gen()

# import sys
# i = 0
# t = int(input())
# for line in sys.stdin:
#     n = int(line)
#     i += 1
#     if i == t: break

#for _ in range(int(sys.stdin.readline())):

#memory with array < memory with list
from math import sqrt

n = int(input())
m = int(sqrt(n))
sang = [i for i in range(m + 1)]
for i in range(2, int(sqrt(m)) + 1):
    if sang[i] == i:
        for j in range(i * i, m + 1, i):
            sang[j] = i

res = 0
for i in range(2, m + 1):
    p = sang[i]
    q = sang[i // sang[i]]
    if p * q == i and q != 1 and p != q: 
        print(i)
        res += 1
    elif sang[i] == i:
        if i ** 8 <= n : res += 1
print(res)






