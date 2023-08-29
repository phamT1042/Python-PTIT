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
        mx_val = n[swap_second]
        for i in range(swap_first + 2, len(n)):
            if n[i] > mx_val and n[i] < n[swap_first]:
                swap_second = i
                mx_val = n[i]
        
        n = n[:swap_first] + n[swap_second] + n[swap_first + 1:swap_second] + n[swap_first] + n[swap_second + 1:]
        print(-1) if n[0] == '0' else print(n)