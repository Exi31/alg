
# UCLN, BCNN

from sys import stdin
from math import gcd

arr = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0: break
    arr.append((a, b))

for tupl in arr:
    a, b = tupl
    ucln = gcd(a, b)
    bcnn = a * b // ucln

    print(ucln, bcnn)