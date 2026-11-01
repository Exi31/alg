
# TÍNH SỐ NGÀY

from sys import stdin
from datetime import date

input = stdin.readline

d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

result = (date2 - date1).days
print(result)