from bisect import bisect_left
import sys
# from math import log

# # This program prints all hcn (highly composite numbers) <= MAXN (=10**9)
# MAXN = 10**9
# # Generates a list of the first primes (with product > MAXN).
# def gen_primes():
# 	primes = []
# 	primes_product = 1
# 	for n in range(2, 10**7):
# 		is_prime = True
# 		for i in range(2, n):
# 			if n % i == 0:
# 				is_prime = False
# 		if is_prime: 
# 			primes.append(n)
# 			primes_product *= n
# 			if primes_product > MAXN: break
# 	return primes
# primes = gen_primes()

# # Generates a list of the hcn <= MAXN.
# def gen_hcn():
#     # List of (number, number of divisors, exponents of the factorization)
# 	hcn = [(1, 1, [])]
# 	for i in range(len(primes)):
# 		new_hcn = []
# 		for el in hcn:
# 			new_hcn.append(el)
# 			if len(el[2]) < i: continue
# 			e_max = el[2][i - 1] if i >= 1 else int(log(MAXN, 2))
# 			n = el[0]
# 			for e in range(1, e_max+1):
# 				n *= primes[i]
# 				if n > MAXN: break
# 				div = el[1] * (e + 1)
# 				exponents = el[2] + [e]
# 				new_hcn.append((n, div, exponents))
# 		new_hcn.sort()
# 		hcn = [(1, 1, [])]
# 		for el in new_hcn:
# 			if el[1] > hcn[-1][1]: hcn.append(el)
# 	res = []
# 	for i in hcn: res.append(i[0])
# 	return res

hcn = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]
t = int(input())
i = 0
for line in sys.stdin :
    n = int(line)
    print(hcn[bisect_left(hcn, n)])
    i += 1
    if i == t: break
