
# TRINH THÁM
# intuition theo kiểu di từng cửa sổ một trong array rồi từng max dùng được nhưng TLE

from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))

q = deque([])       # lưu index của những sinh viên
result = []         # lưu kết quả

for i in range(n):
    # loại những thằng đầu bên trái deque mà out cửa sổ size k (đang tính từ i - k + 1 -> i)
    while q and q[0] <= i - k:
        q.popleft()

    # loại những thằng đầu bên phải queue mà chiều cao <= thằng sắp vào
    while q and heights[q[-1]] <= heights[i]:
        q.pop()

    q.append(i)

    # nếu cửa sổ đủ size k thì append max của cửa sổ (index q[0] - đầu dãy q) vào result
    if i >= k - 1:
        result.append(heights[q[0]])

print(*result)
