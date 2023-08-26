from sys import stdin, stdout

for t in range(int(stdin.readline())):
    s1, s2 = input(), input()
    check = "YES" if sorted(s1) == sorted(s2) else "NO"
    stdout.write("Test {0}: {1}".format(t + 1, check) + "\n")

