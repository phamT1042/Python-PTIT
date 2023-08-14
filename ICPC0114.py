sang = [1 for _ in range(10000000)]
sang[0] = sang[1] = 0
for i in range(2, 3163):
    if sang[i]:
        for j in range(i * i, 10000000, i):
            sang[j] = 0

def check(n):
    if not sang[n]: return "No"
    if not sang[int(str(n)[::-1])]: return "No"
    a = list(map(int, str(n)))
    if not sang[sum(a)]: return "No"
    for i in a:
        if not sang[i]: return "No"
    return "Yes"

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    print(check(n))


    
