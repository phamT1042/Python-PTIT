n, k = map(int, input().split())
a = [""] + list(sorted(set(input().split())))
n = len(a) - 1
sh = [0] * (k + 1)

def Try(i):
    for j in range(sh[i - 1] + 1, n - k + i + 1):
        sh[i] = j
        if i == k: 
            for h in range(1, k + 1): print(a[sh[h]], end = ' ')
            print()
        else: Try(i + 1)

Try(1)
