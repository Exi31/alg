
# ĐẾM TRÊN DÃY SỐ

from math import sqrt
from math import isqrt
from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

k_chia_het_cho_3 = 0
chinh_phuong = 0
cap_2_so = 0
cap_2_so_1 = 0
bo_3_so = 0

for x in arr:
    if x % 3 != 0: k_chia_het_cho_3 += 1
    if (x >= 0 and sqrt(x) == isqrt(x)): chinh_phuong += 1

for i in range(n - 1):
    if (arr[i] != 0) and (arr[i + 1] % arr[i] == 0): cap_2_so += 1

    for j in range(n):
        if i < j:
            if (arr[i] % 2 == 0 and arr[j] % 2 == 0) or (arr[i] % 2 == 1 and arr[j] % 2 == 1):
                cap_2_so_1 += 1

for i in range(n - 2):
    if arr[i] < arr[i + 1] < arr[i + 2]: bo_3_so += 1

print(k_chia_het_cho_3)
print(chinh_phuong)
print(cap_2_so)
print(cap_2_so_1)
print(bo_3_so)