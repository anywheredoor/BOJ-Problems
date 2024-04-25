"""
https://www.acmicpc.net/problem/5532 (방학 숙제)

Mathematics
Arithmetic
"""

import sys

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

math = 0
language = 0

while B > 0:
    B -= D
    math += 1

while A > 0:
    A -= C
    language += 1

print(L - max(math, language))
