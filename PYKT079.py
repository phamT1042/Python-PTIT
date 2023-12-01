t = int(input())
while t > 0:
    t -= 1
    n = input()
    a = list(map(int, input().split()))
    print(max(a) - min(a) + 1 - len(set(a)))