"""
https://www.acmicpc.net/problem/13985 (Equality)

Mathematics
String
Arithmetic
"""
equation = input()

a = int(equation[0])
b = int(equation[4])
c = int(equation[8])

if a + b == c:
    print("YES")
else:
    print("NO")
