#The problem is the same as finding the k-th number 
#that in base n has only zeros and ones.
#=> write k in binary, instead of powers of 2 add powers of n.
from sys import stdin, stdout

MOD = int(1e9) + 7
for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    res = 0
    a = (bin(k))[2:][::-1]
    for i in range(len(a)):
        if a[i] == '1':
            res = (res + pow(n, i) % MOD) % MOD
    stdout.write(str(res) + "\n")
