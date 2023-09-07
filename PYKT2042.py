# Số cách chia các số từ 1 đến 2N thành N nhóm, mỗi nhóm gồm 2 số mà hiệu 2 số 
# trong 1 nhóm bằng hiệu 2 số trong nhóm khác chính là số ước của N.

from sys import stdin, stdout

sang = [0] * 1000001
for i in range(2, 1001):
    if not sang[i]:
        for j in range(i * i, 1000001, i): sang[j] = i

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n < 1: print(0)
    else:
        res = 1
        while sang[n]:
            cnt = 0
            u = sang[n]
            while n % u == 0:
                cnt += 1
                n //= u
            res *= (cnt + 1)
        if n > 1: res *= 2
        stdout.write(str(res) + "\n")

