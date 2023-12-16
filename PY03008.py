from sys import stdin
def stdin_gen():
    for x in stdin.read().split():
        yield int(x)
cin = stdin_gen()

n = next(cin)
ke = [0] * (n)
for i in range(n - 1):
    a, b = next(cin), next(cin)
    ke[a - 1] += 1
    ke[b - 1] += 1

head, res = 0, "Yes"
for i in ke:
    if i == n - 1:
        if head:
            res = "No"
            break
        else: head = 1
    elif i != 1: 
        res = "No"
        break
print(res)