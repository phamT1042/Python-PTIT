from math import gcd
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    save_cost = dict()
    save_gcd = []
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))

    save_cost[a[0]] = c[0]
    save_gcd.append(a[0])
    for i in range(1, n):

        if a[i] not in save_cost: 
            save_cost[a[i]] = c[i]
            save_gcd.append(a[i])
        else: save_cost[a[i]] = min(save_cost[a[i]], c[i])

        for j in save_gcd:
            d = gcd(j, a[i])
            cost = save_cost[j] + c[i]
            if d not in save_cost:
                save_cost[d] = cost
                save_gcd.append(d)
            else: save_cost[d] = min(save_cost[d], cost)
    
    if 1 not in save_cost:
        stdout.write(str(-1) + '\n')
    else:
        stdout.write(str(save_cost[1]) + '\n')
