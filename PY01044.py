a, b = list(input().split()), list(input().split())
a_set, b_set = set(), set()
for i in a: a_set.add(i.lower())
for i in b: b_set.add(i.lower())

for x in sorted(a_set.union(b_set)):
    print(x, end = ' ')
print()
for x in sorted(a_set.intersection(b_set)):
    print(x, end = ' ')