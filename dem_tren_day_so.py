
from math import sqrt

n = int(input("Nhập số phần tử của dãy số: "))

nums = []

for i in range(n):
    x = int(input(f"Nhập phần từ thứ {i + 1}: "))
    nums.append(x)

k_chia_het_cho_3 = chinh_phuong = cap_so = cap_chan_le = bo_ba = 0

for i in range(n):
    if nums[i] % 3 != 0: k_chia_het_cho_3 += 1
    if nums[i] >= 0 and int(sqrt(nums[i])) ** 2 == nums[i]: chinh_phuong += 1

    for j in range(i + 1, n):
        if (nums[i] % 2 == 0 and nums[j] % 2 == 0) or (nums[i] % 2 == 1 and nums[j] % 2 == 1):
            cap_chan_le += 1

for i in range(n - 1):
    if (nums[i] != 0) and (nums[i + 1] % nums[i] == 0): cap_so += 1

for i in range(n - 2):
    if (nums[i] < nums[i + 1] < nums[i + 2]): bo_ba += 1


print(k_chia_het_cho_3)
print(chinh_phuong)
print(cap_so)
print(cap_chan_le)
print(bo_ba)