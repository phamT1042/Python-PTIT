n, k = map(int, input().split())
a = list(map(int, input().split()))
end, can = n - 1, 0
sh, sign = [""] * end, ["+", "-", "*"]

def check():
    global can
    s = ""
    if a[0] < 0: s += "(" + str(a[0]) + ")"
    else: s += str(a[0])
    for i in range(end):
        s += sh[i]
        if a[i + 1] < 0: s += "(" + str(a[i + 1]) + ")"
        else: s += str(a[i + 1])
    if eval(s) == k:
        s += "=" + str(k)
        print(s)
        can = 1

def Try(i):
    for j in sign:
        sh[i] = j
        if i == end - 1: check()
        else: Try(i + 1)

Try(0)
if not can: print("IMPOSSIBLE")

