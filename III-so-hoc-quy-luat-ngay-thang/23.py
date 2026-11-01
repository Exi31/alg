
# CÁNH CỬA THẦN KÌ
# vòng 1: A B C D E                     => 5 * 1
# vòng 2: AA BB CC DD EE                => 5 * 2
# vòng 3: AAAA BBBB CCCC DDDD EEEE      => 5 * 4, cứ nhân đôi lên
# ...
# ta tìm xem x ở vòng nào
# ví dụ x = 20, x qua vòng 1 -> còn 15, x qua vòng 2 -> còn 5, vậy x ở vòng 3
# thấy 5 ở chữ B đầu của vòng 3, tính bằng (5 - 1) // 4 = 1 => index là 1, in names[index] ra

from sys import stdin

input = stdin.readline

names = ["dangdungcntt", "tienquanutc", "quang123", "maianh", "nguyenminhduc2820"]

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

result = []
for x in arr:
    b = 1
    while x > 5 * b:
        x -= 5 * b
        b *= 2

    index = (x - 1) // b
    print(names[index])