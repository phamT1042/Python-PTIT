# Let r1, r2, r3 … be the radii. A right angle triangle with sides s1 and s2 (s2 < s1)
# The area of the triangle is:
# (1/2)r1(s1 + s2 + sqrt(s1^2 + s2^2)) = (1/2)s1s2

# Then (1): 
# r1 = (1/2)(s1 + s2 − sqrt(s1^2 + s2^2)) = (s1/2)(1 + t − sqrt(1 + t^2)) ; t = s2 / s1

# With O is the center of a circle of radius r1. Also, the radii form a geometric series with ratio a (a < 1):

# AO = r1 + 2r2 + 2r3 + ... = 2(r1 + r2 + ...) - r1
#    = (2r1 / (1 − a)) − r1 = sqrt((s1 − r1)^2 + r1^2)

# Find a with (1):
# a=(sqrt((1+sqrt(1+t^(2)))^(2)+t^(2))-t)/(sqrt((1+sqrt(1+t^(2)))^(2)+t^(2))+t)

# The total area, thus, is
# A = pi(r1^2 + r2^2 + ...) = (pi * r1^2)/(1 - a^2)=(pi(s1+s2-sqrt(s1^2 + s2^2))^2)/(4(1-a^2))
from math import sqrt, pi

s2, s1 = map(int, input().split())
t = s2 / s1
a = (sqrt(pow(1+sqrt(1+t*t),2)+t*t)-t)/(sqrt(pow(1+sqrt(1+t*t),2)+t*t)+t)
A = (pi*pow(s1+s2-sqrt(s1*s1 + s2*s2),2))/(4*(1-a*a))
print("%.4f" % (A / ((1/2) * s1 * s2)))