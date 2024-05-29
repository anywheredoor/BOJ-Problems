"""
https://www.acmicpc.net/problem/25238 (가희와 방어율 무시)

Mathematics
Arithmetic
"""
a, b = map(int, input().split())

c = a - a * (b / 100)

if c >= 100:
    print(0)
else:
    print(1)
