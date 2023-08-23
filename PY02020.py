n = int(input())
a = list(map(float, input().split()))
i, j = 1, n - 2
a.sort()
while a[i] == a[i - 1]: i += 1
while a[j] == a[j + 1]: j -= 1
print("{0:.2f}".format(sum(a[i : j + 1]) / (j - i + 1)))