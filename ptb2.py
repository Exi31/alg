
from math import sqrt

a, b, c = map(float, input("Nhập a, b, c của phương trình bậc 2: ").split())

delta = b ** 2 - 4 * a * c

if a == b == c == 0: print("Phương trình vô số nghiệm")
elif delta < 0: print("Phương trình vô nghiệm")
elif delta == 0:
    print(f"Phương trình có 1 nghiệm kép: {-b / (2 * a)}")
else:
    print(f"Phương trình có 2 nghiệm phân biệt: {(-b + sqrt(delta)) / (2 * a)} và {(-b - sqrt(delta)) / (2 * a)}")