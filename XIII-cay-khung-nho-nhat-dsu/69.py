
# CÂY KHUNG NHỎ NHẤT (PRIM)

import heapq

n, m = map(int, input().split())    # đồ thị có n đỉnh, m cạnh
arr = []

for i in range(m):
    u, v, w = map(int, input().split())         # u, v là 2 đỉnh đầu mút; w là trọng số của cạnh
    arr.append((u, v, w))

# lưu danh sách các điểm kề của từng điểm
adj = [[] for _ in range(i + 1)]
for u, v, w in arr:
    adj[u].append((v, w))
    adj[v].append((u, w))

# lưu trạng thái của từng điểm, tổng trọng số của đồ thị
visited = [False] * (n + 1)
total = 0
heap = [(0, 1)]     # heap lưu trữ (trọng số, điểm)

# bắt đầu nối các đoạn có trọng số nhỏ nhất
while heap:
    w, u = heapq.heappop(heap)

    if visited[u]:
        continue

    visited[u] = True
    total += w

    for v, w in adj[u]:
        if visited[v]:
            continue

        heapq.heappush(heap, (w, v))

print(total)