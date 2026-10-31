
# TÍNH TỔNG TRÊN DÃY SỐ NGUYÊN

from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
total = 0

for i in range(1, n + 1):
    total += sum(arr[0:i])

print(total)