
# BỘ BA PYTAGO
# gọi r là cạnh mới của tam giác
# r có thể là cạnh huyền: r^2 = a^2 + b^2
# r có thể là cạnh góc vuông: r^2 = abs(a^2 - b^2)
# kết quả d nhỏ nhất có thể, nếu d không tồn tại thì in -1

from sys import stdin
from math import isqrt

input = stdin.readline

a, b, c = map(int, input().split())
best = -1

for x, y, z in [(a, b, c), (b, a, c), (c, a, b)]:
    for square in [y ** 2 + z ** 2, abs(y ** 2 - z ** 2)]:
        r = isqrt(square)

        if r > 0 and r ** 2 == square:
            d = abs(x - r)

            if best == -1 or d < best:
                best = d

print(best)