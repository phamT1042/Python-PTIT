def merge(a, l, m, r):
    tmp1, tmp2 = a[l:m+1], a[m+1:r+1]
    i, j, cnt = 0, 0, 0
    while i < len(tmp1) and j < len(tmp2):
        if tmp1[i] <= tmp2[j]:
            a[l] = tmp1[i]
            l, i = l + 1, i + 1
        else:
            cnt += len(tmp1) - i
            a[l] = tmp2[j]
            l, j = l + 1, j + 1

    while i < len(tmp1): 
        a[l] = tmp1[i]
        l, i = l + 1, i + 1
    while j < len(tmp2): 
        a[l] = tmp2[j]
        l, j = l + 1, j + 1

    return cnt

def merge_sort(a, l, r):
    cnt = 0
    if l < r:
        m = (l + r) // 2
        cnt += merge_sort(a, l, m)
        cnt += merge_sort(a, m + 1, r)
        cnt += merge(a, l, m, r)
    return cnt

n = int(input())
a = list(map(int, input().split()))
print(merge_sort(a, 0, n - 1))