
# PHÂN LOẠI CÁC F CÁCH LY C19

from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())

tiep_xuc = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    tiep_xuc[x].append(y)
    tiep_xuc[y].append(x)

f = [-1] * (n + 1)

k = int(input())
f0 = list(map(int, input().split()))
for x in f0:
    f[x] = 0

q = deque(f0)
checked = set(f0)

while q:
    person = q.popleft()

    for pers in tiep_xuc[person]:
        if pers in checked: continue

        checked.add(pers)
        q.append(pers)
        f[pers] = f[person] + 1


for i in range(0, max(f) + 1):
    print(f"F{i}: {f.count(i)}")
