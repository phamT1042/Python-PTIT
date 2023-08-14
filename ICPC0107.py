import sys

def stdin_gen():
    for x in sys.stdin.read().split():
        yield x

cin = stdin_gen()

t = int(next(cin))
while t > 0:
    t -= 1
    a, b, x1, x2 = next(cin), next(cin), next(cin), next(cin)
    Min, Max = min(a, b), max(a, b)
    print(int(x1.replace(Max, Min)) + int(x2.replace(Max, Min)), int(x1.replace(Min, Max)) + int(x2.replace(Min, Max)))