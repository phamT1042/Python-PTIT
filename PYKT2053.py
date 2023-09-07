for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if sum(a) % 3: 
        print(0)
        continue
    
    vs = [0] * n
    res, sum_child = 0, sum(a) // 3
    def Try(i, sum, cnt):
        global res
        if cnt == 2:
            res += 1
            return
        
        if sum == sum_child: 
            Try(0, 0, cnt + 1)
            return
        elif sum > sum_child: return

        for j in range(i, n):
            if not vs[j]:
                vs[j] = 1
                Try(j + 1, sum + a[j], cnt)
                vs[j] = 0

    Try(0, 0, 0)
    print(res)
