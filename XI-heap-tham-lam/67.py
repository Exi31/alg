
# GIAO HÀNG

import heapq

n = int(input())
orders = []

for i in range(n):
    t, v = map(int, input().split())
    orders.append((t, v))

orders.sort(key=lambda arr: arr[0])

chosen = []

for i in range(n):
    heapq.heappush(chosen, orders[i][1])

    if orders[i][0] < len(chosen):
        heapq.heappop(chosen)

print(sum(chosen))