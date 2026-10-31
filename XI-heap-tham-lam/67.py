
# GIAO HÀNG

from sys import stdin
import heapq

input = stdin.readline

orders = []
n = int(input())

for _ in range(n):
    t, v = map(int, input().split())
    orders.append((t, v))

orders.sort(key=lambda arr: arr[0])

chosen = []     # min-heap chứa tiền thưởng của các món đang chọn


# thử nhận thêm một đơn, nếu không giao kịp thì bỏ đơn ít giá trị nhất
for t, v in orders:
    heapq.heappush(chosen, v)

    if len(chosen) > t:
        heapq.heappop(chosen)

print(sum(chosen))