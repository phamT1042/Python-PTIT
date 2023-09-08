def check(n, base):
    num = ""
    while n:
        num += str(n % base)
        n //= base
    return num == num[::-1]

def check_bin(n):
    bir = bin(n)[2:]
    return bir == bir[::-1]

a, b, m = map(int, input().split())
res = [i for i in range(a, b + 1) if check_bin(i)]
for i in range(3, m + 1):
    res = [j for j in res if check(j, i)]
    if len(res) == 0: break
print(len(res))