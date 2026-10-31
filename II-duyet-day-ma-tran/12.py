
# TÍNH CHẤT ĐƠN ĐIỆU CỦA DÃY SỐ

from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

bang_nhau = True
tang_ngat = True
giam_ngat = True
tang = True
giam = True

for i in range(n - 1):
    if arr[i] != arr[i + 1]: bang_nhau = False
    if arr[i] >= arr[i + 1]: tang_ngat = False
    if arr[i] <= arr[i + 1]: giam_ngat = False
    if arr[i] > arr[i + 1]: tang = False
    if arr[i] < arr[i + 1]: giam = False

if bang_nhau: print("Day bang nhau")
elif tang_ngat: print("Day don dieu tang ngat")
elif giam_ngat: print("Day don dieu giam ngat")
elif tang: print("Day don dieu tang")
elif giam: print("Day don dieu giam")
else: print("Day khong don dieu")