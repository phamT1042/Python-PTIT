import math

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    sh, used = [0] * n, [0] * n

    def Try(i):
        for j in range(n, 0, -1):
            if not used[j - 1]:
                used[j - 1] = 1
                sh[i] = j
                if i == n - 1: 
                    for k in sh: print(k, end = '')
                    print(' ', end = '')
                else: Try(i + 1)
                used[j - 1] = 0 
    
    print(math.factorial(n))
    Try(0)
    print()