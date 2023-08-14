import math
t = int(input())
while t > 0:
    t -= 1
    b, s = input(), input()

    extra = int(math.log2(int(b)))
    res, i = "", 0

    if len(s) % extra:
        i += len(s) % extra
        res += str(int(s[:i], 2))

    while i < len(s):
        change = int(s[i:i+extra], 2)
        if change < 10:
            res += str(change)
        else:
            res += chr(change+55)
        i += extra
        
    print(res)