
# LÀM BÀI TẬP

from sys import stdin

input = stdin.readline

a, b, c, d = map(int, input().split())

result = min(b, d) - max(a, c)
result = result if result >= 0 else 0

print(result)