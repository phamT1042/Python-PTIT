import sys
import array
#dùng arr giảm memory hơn list
#dùng sys tăng thời gian input

mx = int(2e6) + 1
sang = array.array('i', [0] * mx)
i = 2
while i * i < mx:
    if not sang[i]:
        sang[i] = i
        for j in range(i * i, mx, i):
            sang[j] = i
    i += 1
for i in range(4, mx):
    sang[i] += sang[i // sang[i]] if sang[i] else i

res = 0
for _ in range(int(sys.stdin.readline())):
    res += sang[int(sys.stdin.readline())]
print(res)