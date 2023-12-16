t = int(input())
while t > 0:
    t -= 1
    n = input()
    swap_first = -1
    for i in range(len(n) - 2, -1, -1):
        if n[i] > n[i + 1]: 
            swap_first = i
            break
    if swap_first == -1:
        print(-1)
    else:
        swap_second = swap_first + 1
        for i in range(len(n) - 1, swap_first, -1):
            if n[i] < n[swap_first]:
                j = i
                while n[j] == n[i]: j -= 1
                swap_second = j + 1
                break
        
        n = n[:swap_first] + n[swap_second] + n[swap_first + 1:swap_second] + n[swap_first] + n[swap_second + 1:]
        print(-1) if n[0] == '0' else print(n)