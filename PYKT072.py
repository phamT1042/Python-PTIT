save = []
n = int(input())
for _ in range(n):
    save.append(input())

sh = dict()
cnt, tmp = 1, save[0]
while 1:
    if tmp in sh: break
    sh[tmp] = cnt
    tmp, cnt = tmp[1:] + tmp[0], cnt + 1

flag, res = 1, 2501
for choose in sh:
    sm, j = 0, sh[choose]
    for string in save:
        if string not in sh: 
            flag = 0
            break
        i = sh[string]
        if j >= i: sm += j - i 
        else: sm += len(sh) - i + j
    res = min(res, sm)

print(res) if flag else print(-1)