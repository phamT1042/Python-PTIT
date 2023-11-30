d1, d2 = set(), set()

f = open("DATA1.in", "r")
for line in f.readlines():
    for char in line.split():
        d1.add(char.lower())
f.close()

f = open("DATA2.in", "r")
for line in f.readlines():
    for char in line.split():
        d2.add(char.lower())
f.close()

print(*sorted(d1 - d2))
print(*sorted(d2 - d1))