
# LẠI LÀ LẬT MẶT CÁC ĐỒNG XU
# default: ngửa
# => lật n chẵn lần -> vẫn ngửa, lật n lẻ lần -> sấp
# số chính phương có n lẻ ước, các số còn lại có n chẵn ước
# số đồng xu ngửa = n - isqrt(n) (isqrt(n) là số số chính phương)

from sys import stdin
from math import isqrt

n = int(input())
arr = list(map(int, input().split()))

for x in arr:
    print(x - isqrt(x))