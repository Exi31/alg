
# BỘI SỐ CỦA 13

from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())

total = 0

a = min(n, m)
b = max(n, m)

for i in range(a, b + 1):
    if i % 13 == 0: continue

    total += i

print(total)