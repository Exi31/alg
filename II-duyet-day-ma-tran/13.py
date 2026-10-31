
# CÁC ĐƯỜNG CHÉO SONG SONG VỚI ĐƯỜNG CHÉO CHÍNH & PHỤ CỦA MA TRẬN
# trên đường chéo song song với đường chéo chính: hiệu x - y luôn như nhau
# trên đường chéo song song với đường chéo phụ: tổng x + y luôn như nhau

from sys import stdin

input = stdin.readline

n, q = map(int, input().split())
matrix = []
points = []
result = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for _ in range(q):
    x, y = map(int, input().split())
    points.append((x, y))


for tupl in points:
    x, y = tupl
    total = 0
    smallest = matrix[x - 1][y - 1]

    for a in range(n):
        for b in range(n):
            if (a - b == x - y): total += matrix[a][b]
            if (a + b == x + y - 2): 
                if matrix[a][b] < smallest: smallest = matrix[a][b]

    result.append((total, smallest))

for tupl in result:
    total, smallest = tupl
    print(total, smallest, sep=" ")

