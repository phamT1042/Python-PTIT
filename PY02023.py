t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(input().split())
    a.sort(key = lambda x: (sum([int(i) for i in x]), len(x), x))
    for x in a: print(x, end = ' ')
    print()