
# VÒNG LẶP

strr = input()
n = len(strr)

s1 = 9
s2 = s1 + 90 * 2
s3 = s2 + 900 * 3
s4 = s3 + 9000 * 4
s5 = s4 + 90000 * 5

if n <= s1: result = n
elif s1 < n <= s2: result = (n - s1) // 2 + 9
elif s2 < n <= s3: result = (n - s2) // 3 + 99
elif s3 < n <= s4: result = (n - s3) // 4 + 999
elif s4 < n <= s5: result = (n - s4) // 5 + 9999

print(result)