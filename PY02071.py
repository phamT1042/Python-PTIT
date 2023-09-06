a = [0] * 12
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a[1] = n
    res, flag, cnt = [], 0, 1

    def split():
        global flag, cnt
        i = cnt
        while a[i] == 1: i -= 1
        if i == 0: 
            flag = 1
            return
        a[i] -= 1
        number1_is_skipped = cnt - i + 1
        cnt = i
        q, r = number1_is_skipped // a[i], number1_is_skipped % a[i]
        for j in range(1, q + 1):
            cnt += 1
            a[cnt] = a[i]
        if r:
            cnt += 1
            a[cnt] = r

    while 1:
        split()
        if flag: break
        save = "("
        for i in range(1, cnt + 1):
            save += str(a[i])
            if i < cnt: save += " "
        res.append(save + ")")

    print(len(res) + 1)
    print("({0})".format(n), end = ' ')
    for x in res:
        print(x, end = ' ')
    print()
