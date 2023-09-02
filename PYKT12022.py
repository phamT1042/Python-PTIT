from sys import stdin, stdout

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

curr_val, res = set(), set()
for i in a:
    change_val = set()
    res.add(i)
    change_val.add(i)
    for j in curr_val:
        change_val.add(i | j)
        res.add(i | j)
    curr_val = change_val
    
stdout.write(str(len(res)))