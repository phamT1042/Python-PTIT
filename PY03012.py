n = int(input())
save = []
for i in range(n):
    s = input()
    ac, submit = map(int, input().split())
    save.append((s, ac, submit))

save.sort(key=lambda x: (-x[1], x[2], x[0]))
for tup in save:
    print(tup[0], tup[1], tup[2])
