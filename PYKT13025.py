n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = dict()
for i in a:
    if i not in cnt: cnt[i] = 1
    else: cnt[i] += 1
people_per_legion = sorted(cnt.values())
people_per_legion.insert(0, 0)

def cal(capacity):
    number_car, l, r = 0, 1, k
    while l <= r:
        number_car += 1
        if people_per_legion[l] + people_per_legion[r] > capacity:
            r -= 1
        else:
            l += 1
            r -= 1
    return number_car * capacity 

res = float('inf')
for capacity in range(people_per_legion[-1], people_per_legion[-1] + 1001):
    fee = cal(capacity)
    if res > fee: res = fee
print(res)