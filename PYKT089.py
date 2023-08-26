import sys
def stdin_gen():
    for x in sys.stdin.read().split():
        yield int(x)
cin = stdin_gen()

n = int(input())
a, even, odd = [], [], []
for _ in range(n):
    x = next(cin)
    a.append(x)
    if x & 1: odd.append(x)
    else: even.append(x)

even.sort()
odd.sort(reverse = True)
j, k = 0, 0
for i in a:
    if i & 1:
        print(odd[k], end = ' ')
        k += 1
    else:
        print(even[j], end = ' ')
        j += 1