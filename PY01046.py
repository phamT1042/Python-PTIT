n = int(input())

def Try(n, a, b, c):
    if n == 1:
        print("{0} -> {1}".format(a, c))
    else:
        Try(n - 1, a, c, b)
        Try(1, a, b, c)
        Try(n - 1, b, a, c)

Try(n, 'A', 'B', 'C')