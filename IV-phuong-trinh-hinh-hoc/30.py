
# CHU VI & DIỆN TÍCH ĐA GIÁC LỒI

from sys import stdin
from math import sqrt

input = stdin.readline

n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

x1, y1 = points[0]
x2, y2 = points[-1]

chu_vi = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
dien_tich = (x1 * y2 - x2 * y1) * (-1)

for i in range(n - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]

    chu_vi += sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    dien_tich += x1 * y2 - x2 * y1

print(f"{chu_vi:.3f}")

dien_tich = abs(dien_tich / 2)
print(f"{dien_tich:.3f}")