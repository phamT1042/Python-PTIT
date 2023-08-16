t = int(input())
while t > 0:
    t -= 1
    a = input()
    if len(a) == 1: print(a)
    else:
        i, memo, res = len(a) - 1, 0, ""
        while i > 0:
            tmp = int(a[i]) + memo
            memo = 1 if tmp >= 5 else 0
            res = "0" + res
            i -= 1
        res = str(int(a[i]) + memo) + res
        print(res) 