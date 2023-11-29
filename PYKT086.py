import math

inp = open("DATA.in", "r")
n = int(inp.readline())
for i in range(n):
    b = int(inp.readline())
    s = inp.readline().rstrip('\n')

    extra = int(math.log2(b))
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
inp.close()
