t = int(input())
save = [str(i) for i in range(0, 10)] + [chr(i) for i in range(65, 91)]

while t > 0:
    t -= 1
    n, k = map(int, input().split())

    res = ""
    while n:
        res = save[n % k] + res
        n //= k
    print(res)

