
# DÃY CON LIÊN TỤC KHÁC BIỆT

n = int(input())
arr = list(map(int, input().split()))

last = {}       # lưu trữ index cuối cùng xuất hiện của một số
left = 0        # cửa sổ [left, i] k có phần tử trùng
best = 0        # độ dài đoạn dài nhất

for i, x in enumerate(arr):
    if x in last and last[x] >= left:
        left = last[x] + 1
    last[x] = i
    best = max(best, i - left + 1)

print(best)