"""
https://www.acmicpc.net/problem/16199 (나이 계산하기)

Mathematics
Implementation
Arithmetic
"""
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

a1 = 0

if y2 > y1:
    a1 = y2 - y1 - 1
    
    if m2 > m1:
        a1 = y2 - y1

    if m2 == m1 and d2 >= d1:
        a1 = y2 - y1

a2 = y2 - y1 + 1

a3 = y2 - y1

print(a1)
print(a2)
print(a3)
