
# NHÀ SOẠN NHẠC TÀI BA

from sys import stdin

input = stdin.readline

tang = True
giam = True

arr = list(map(int, input().split()))

for i in range(len(arr) - 1):
    if arr[i] >= arr[i + 1]: tang = False
    if arr[i] <= arr[i + 1]: giam = False

if tang: print("TANG")
elif giam: print("GIAM")
else: print("KHONGBIET")