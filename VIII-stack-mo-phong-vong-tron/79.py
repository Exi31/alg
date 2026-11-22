
# XẾP HÀNG

n = int(input())
heights = list(map(int, input().split()))

result = 0

stack = []
for i in range(n):
    while stack and heights[i] > stack[-1][0]:
        height, count = stack.pop()
        result += count

    if stack and heights[i] == stack[-1][0]:
        height, count = stack.pop()

        result += count

        if len(stack) >= 1:
            result += 1

        stack.append((heights[i], count + 1))

    if stack and heights[i] < stack[-1][0]:
        result += 1
        stack.append((heights[i], 1))

    if len(stack) == 0:
        stack.append((heights[i], 1))

print(result)