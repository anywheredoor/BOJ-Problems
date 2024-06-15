"""
https://www.acmicpc.net/problem/17009 (Winning Score)

Mathematics
Implementation
Arithmetic
"""
a = 0
b = 0

p = 3
for _ in range(3):
    a += int(input()) * p
    p -= 1

p = 3
for _ in range(3):
    b += int(input()) * p
    p -= 1

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("T")
