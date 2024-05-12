"""
https://www.acmicpc.net/problem/11948 (과목선택)

Mathematics
Implementation
Arithmetic
"""

import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
E = int(sys.stdin.readline())
F = int(sys.stdin.readline())

first = sum((A, B, C, D)) - min(A, B, C, D)
second = max(E, F)

print(first + second)
