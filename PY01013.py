import math

def is_prime(n):
    if n < 2: return "NO"
    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i: return "NO"
    return "YES"

t = int(input())
while t > 0:
    t -= 1
    a, b = map(int, input().split())
    Sum = sum(int(i) for i in str(math.gcd(a, b)))
    print(is_prime(Sum))