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

def powMod(a, b, m):
    res = 1
    while b:
        if b & 1:
            res *= a
            res %= m
        a *= a
        a %= m
        b //= 2
    return res

for _ in range(int(input())):
    a, b, m = map(int, input().split())
    x, l, r = pow(10, 10), 0, pow(10, 10)

    while l <= r:
        mid = (l + r) // 2
        if powMod(a, mid, m) == b:
            x, r = mid, mid - 1
        else:
            l = mid + 1
    print(x)




        



