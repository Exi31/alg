
# K59

n = int(input())
heights = list(map(int, input().split()))

L = [-1] * n
R = [-1] * n

stack = []
for i in range(n):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()

    if len(stack) != 0: L[i] = stack[-1]

    stack.append(i)

stack = []
for i in range(n - 1, -1, -1):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()

    if len(stack) != 0: R[i] = stack[-1]

    stack.append(i)

result = [-1] * n
for i in range(n):
    if L[i] == R[i] == -1: continue
    elif L[i] != -1 and R[i] == -1: result[i] = L[i]
    elif R[i] != -1 and L[i] == -1: result[i] = R[i]
    else:
        closest_left = i - L[i]
        closest_right = R[i] - i

        if closest_left <= closest_right: result[i] = L[i]
        else: result[i] = R[i]

print(*result)
