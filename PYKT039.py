for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    res = "YES"
    for i in range(n):
        if a[i] > b[i]: 
            res = "NO"
            break
    print(res)