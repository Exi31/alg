
# PHƯƠNG TRÌNH BẬC HAI

from sys import stdin
from math import sqrt

input = stdin.readline

a, b, c = map(float, input().split())

if a == 0:
    if b == 0:
        if c == 0: print("vo so nghiem")
        else: print("vo nghiem")

    else:
        print(f"{(-c / b):.3f}")

else:
    delta = b ** 2 - 4 * a * c

    if delta < 0: print("vo nghiem")
    elif delta == 0: print(f"{(-b / (2 * a)):.3f}")
    else:
        X1 = (-b - sqrt(delta)) / (2 * a)
        X2 = (-b + sqrt(delta)) / (2 * a)

        x1 = min(X1, X2)
        x2 = max(X1, X2)

        print(f"{x1:.3f}")
        print(f"{x2:.3f}")