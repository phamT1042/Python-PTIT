import math
def is_prime(num):
    if (n == 1): return False
    end = int(math.sqrt(num))
    for i in range(2, end + 1):
        if not num % i: return False
    return True

def check(n):
    if not is_prime(n): return "No"
    if not is_prime(int(str(n)[::-1])): return "No"
    a = list(map(int, str(n)))
    sum = 0
    for i in a:
        if not is_prime(i): return "No"
        sum += i
    return "Yes" if is_prime(sum) else "No"

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    print(check(n))
        
