n = int(input())
res = []
for i in range(n):
    res.append(input())
hang, cot = [0] * n, [0] * n
for i in range(n):
    for j in range(n):
        if res[i][j] == 'C':
            hang[i], cot[j] = hang[i] + 1, cot[j] + 1
            
choose = 0
for i in range(n): 
    if hang[i] > 1: choose += (hang[i] * (hang[i] - 1)) // 2
    if cot[i] > 1: choose += (cot[i] * (cot[i] - 1)) // 2
    
print(choose)
