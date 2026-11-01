
# SỐ CHIA HẾT LỚN NHẤT

from sys import stdin

input = stdin.readline

a, b = map(int, input().split())

c = (a - 1) // b
result = c * b

print(result)