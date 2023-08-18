t = int(input())

while t > 0: 
    t -= 1
    n, save = int(input()), dict()
    for i in range(2, n + 1):
        if n % i == 0:
            while not n % i:
                if i not in save: save[i] = 1
                else: save[i] += 1
                n /= i
        if n == 1: break
    res = "1 * "
    for key in save:
        res += str(key) + "^" + str(save[key]) + " * "
    print(res[:len(res) - 2])
