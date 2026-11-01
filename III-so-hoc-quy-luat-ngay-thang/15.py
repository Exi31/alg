
# TÍCH CỦA DÃY CẤP SỐ CỘNG

from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
modulo = n % m

result = 1

for i in range(modulo, n + 1, m):
    if i == 0: continue
    result *= i

print(result)