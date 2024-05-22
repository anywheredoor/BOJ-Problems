"""
https://www.acmicpc.net/problem/14489 (치킨 두 마리 (...))

Mathematics
Implementation
Arithmetic
"""

A, B = map(int, input().split())
C = int(input())

total = A + B
two_chickens = 2 * C

if total >= two_chickens:
    print(total - two_chickens)
else:
    print(total)
