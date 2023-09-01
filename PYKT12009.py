from sys import stdin, stdout

n = int(stdin.readline())
a = list(map(float, stdin.readline().split()))

def binary_search_Kadane(x):
    sum_pos, max_sum_pos = 0.0, 0.0
    sum_neg, min_sum_neg = 0.0, 0.0
    for i in a:
        sum_pos += i - x
        sum_neg += i - x

        if sum_pos > 0.0:
            if max_sum_pos < sum_pos: max_sum_pos = sum_pos
        else: sum_pos = 0.0

        if sum_neg < 0.0:
            if min_sum_neg > sum_neg: min_sum_neg = sum_neg
        else: sum_neg = 0.0

    return round(max_sum_pos, 6), round(-min_sum_neg, 6)    

sum_max_pos, sum_max_neg = 1.0, -1.0 
l, r = min(a), max(a)
while sum_max_neg != sum_max_pos:
    m = (l + r) / 2
    sum_max_pos, sum_max_neg = binary_search_Kadane(m)
    if sum_max_pos > sum_max_neg: l = m
    else: r = m

stdout.write("%.6f" % (sum_max_pos))