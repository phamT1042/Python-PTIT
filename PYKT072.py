def solve(n, save):
    l = len(save[0])
    res, end, check = 2501, save[0], 1
    for i in range(l):
        brow = 0
        for j in range(n):
            tmp = save[j]
            for k in range(l):
                if tmp == end:
                    brow += k
                    break
                tmp = tmp[1::] + tmp[0]
            if tmp != end: check = 0
        res = min(res, brow)
        end = end[1::] + end[0]
    return res if check == 1 else -1
                
save = []
n = int(input())
for _ in range(n):
    save.append(input())

print(solve(n, save))







