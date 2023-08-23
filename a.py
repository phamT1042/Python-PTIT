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

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(input().split())
    a.sort(key = lambda x: (sum([int(i) for i in x]), len(x), x))
    for x in a: print(x, end = ' ')
    print()