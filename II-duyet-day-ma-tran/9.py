
# DÃY FIBONACCI ĐƠN GIẢN

from sys import stdin

input = stdin.readline

fibo = [0, 1]
n = int(input())

if n == 1: print(0)
else:
    for i in range(2, n):
        x = fibo[i - 2]
        y = fibo[i - 1]

        fibo.append(x + y)

    print(*fibo)