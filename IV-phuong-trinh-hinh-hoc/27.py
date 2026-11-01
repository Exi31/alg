
# GIẢI VÀ BIỆN LUẬN PHƯƠNG TRÌNH TRÙNG PHƯƠNG

from sys import stdin
from math import sqrt

input = stdin.readline

a, b, c = map(float, input().split())

result = set()
count = 0

if a == 0:
    if b == 0:
        if c == 0: count = -1

    else:
        if b * c <= 0:      # b và c phải khác dấu thì x^2 mới >= 0
            result.add(sqrt(-c / b))
            result.add(-sqrt(-c / b))

else:
    delta = b ** 2 - 4 * a * c

    if delta == 0:
        t = -b / (2 * a)

        if t >= 0:
            result.add(sqrt(t))
            result.add(-sqrt(t))

    elif delta > 0:
        t1 = (-b + sqrt(delta)) / (2 * a)
        t2 = (-b - sqrt(delta)) / (2 * a)

        for t in [t1, t2]:
            if t < 0: continue

            result.add(sqrt(t))
            result.add(-sqrt(t))

count = len(result) if len(result) > 0 else count

if count == -1: print("vo so nghiem")
elif count == 0: print("vo nghiem")
else:
    for x in result:
        print(f"{x:.3f}")