t = int(input())
while t > 0:
    t -= 1
    n, flag = int(input()), 1
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] > b[i]: 
            flag = 0
            break
    print("NO") if not flag else print("YES")