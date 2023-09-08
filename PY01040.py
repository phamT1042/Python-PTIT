for _ in range(int(input())):
    s = list(input())
    n = len(s)
    s1, s2 = s[:n//2], s[n//2:]
    rotate1, rotate2 = 0, 0
    for i in range(n // 2):
        rotate1 += ord(s1[i]) - 65
        rotate2 += ord(s2[i]) - 65
    for i in range(n // 2):
        s1[i] = chr((ord(s1[i]) - 65 + rotate1) % 26 + 65)
        s2[i] = chr((ord(s2[i]) - 65 + rotate2) % 26 + 65)
    for i in range(n // 2):
        s1[i] = chr((ord(s1[i]) - 65 + ord(s2[i]) - 65) % 26 + 65)
    print(''.join(s1))