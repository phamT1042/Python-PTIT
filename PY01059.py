t = int(input())
while t > 0:
    t -= 1
    n = input()
    sum, multi, check = 0, 1, 0
    for i in range(len(n)):
        if i & 1:
            if int(n[i]) != 0:
                check = 1
                multi *= int(n[i])
        else:
            sum += int(n[i])
    if not check: multi = 0
    print(sum, multi)
