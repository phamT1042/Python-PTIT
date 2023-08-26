from collections import OrderedDict
from sys import stdin, stdout

inf = OrderedDict()

def fee(s, n):
    if s == 'Xe_con':
        return 10000 if n == '5' else 15000
    if s == 'Xe_khach':
        return 50000 if n == '29' else 70000
    return 20000

for _ in range(int(stdin.readline())):
    a = stdin.readline().split()
    if a[3][0] == 'O': continue
    if a[4] not in inf:
        inf[a[4]] = fee(a[1], a[2])
    else:
        inf[a[4]] += fee(a[1], a[2])
    
for key in inf:
    print("{0}: {1}".format(key, inf[key]))



