from sys import stdin, stdout

def merge(l, m, r):
    x, y = a[l : m + 1], a[m + 1 : r + 1]
    i, j, cnt = 0, 0, 0
    while i < len(x) and j < len(y):
        if x[i] > y[j]:
            cnt += len(x) - i
            a[l] = y[j]
            l, j = l + 1, j + 1
        else:
            a[l] = x[i]
            l, i = l + 1, i + 1

    while i < len(x): 
        a[l] = x[i]
        l, i = l + 1, i + 1
    while j < len(y):
        a[l] = y[j]
        l, j = l + 1, j + 1

    return cnt

def mergeSort(l, r):
    cnt = 0
    if l < r:
        m = (l + r) >> 1
        cnt += mergeSort(l, m)
        cnt += mergeSort(m + 1, r)
        cnt += merge(l, m, r)
    return cnt

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

stdout.write(str(mergeSort(0, n - 1)))