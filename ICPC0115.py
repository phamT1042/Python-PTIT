import math
t = int(input())
while t > 0:
    t -= 1
    a = input()
    if sum([math.factorial(int(i)) for i in a]) == int(a): print("Yes")
    else: print("No")