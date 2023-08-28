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

n = int(input())
a = list(map(int, input().split()))
tmp, res, mx = 0, 0, max(a)
for i in a:
    if i == mx:
        tmp += 1
    else:
        res = max(res, tmp)
        tmp = 0
print(max(res, tmp))
