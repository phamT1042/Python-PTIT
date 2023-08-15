import math

def is_prime(k):
    if k <= 1: return "NO"
    for i in range(2, int(math.sqrt(k)) + 1):
        if not k % i: return "NO"
    return "YES"

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    k, i = n, 2
    while n > 1:
        if not n % i:
            k *= (i - 1) / i
            while not n % i: n /= i
        i += 1
    print(is_prime(int(k)))
    
