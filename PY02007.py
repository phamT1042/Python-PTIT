import sys
res = set()

def stdin_gen():
    for x in sys.stdin.read().split():
        yield int(x)
cin = stdin_gen()

for i in range(10):
    res.add(next(cin) % 42)
print(len(res))