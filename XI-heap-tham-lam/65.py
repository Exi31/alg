
# HUFFMAN

import heapq

s = input()
freq = {}

for c in s:
    freq[c] = freq.get(c, 0) + 1

heap = list(freq.values())
heapq.heapify(heap)

result = 0
if len(heap) <= 1: result = sum(heap)
else:
    while len(heap) >= 2:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        result += (a + b)
        heapq.heappush(heap, a + b)

print(result)