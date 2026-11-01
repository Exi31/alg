
# GHÉP HÌNH

a, b = map(int, input().split())
c, d = map(int, input().split())

if a == c and b + d == a: print("YES")
elif a == d and b + c == a: print("YES")
elif b == c and a + d == b: print("YES")
elif b == d and a + c == b: print("YES")
else: print("NO")