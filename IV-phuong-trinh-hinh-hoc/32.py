
# HỆ BA PHƯƠNG TRÌNH TUYẾN TÍNH

from sys import stdin

input = stdin.readline

def calc(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

def thay_cot(matrix, cot, ve_phai):
    new_matrix = [row.copy() for row in matrix]

    new_matrix[0][cot] = ve_phai[0]
    new_matrix[1][cot] = ve_phai[1]
    new_matrix[2][cot] = ve_phai[2]

    return new_matrix

abc = []
d = []

for _ in range(3):
    x, y, z, m = map(float, input().split())

    abc.append([x, y, z])
    d.append(m)

D = calc(abc)
Dx = calc(thay_cot(abc, 0, d))
Dy = calc(thay_cot(abc, 1, d))
Dz = calc(thay_cot(abc, 2, d))

if D == 0:
    print("HE PHUONG TRINH SUY BIEN")

else:
    print(f"x = {(Dx / D):.3f}")
    print(f"y = {(Dy / D):.3f}")
    print(f"z = {(Dz / D):.3f}")


