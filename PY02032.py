s, res = input(), set()
for i in range(0, len(s) - 1, 2):
    res.add(s[i] + s[i + 1])
print(*sorted(res))