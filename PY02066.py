import sys
def stdin_gen():
    for x in sys.stdin.read().split():
        yield int(x)
cin = stdin_gen()

n = next(cin)
res, start = [], 1
while n > 0:
    n -= 1
    a = next(cin)
    while start < a: 
        res.append(start)
        start += 1
    start += 1
print(*res, sep = '\n') if len(res) else print("Excellent!")