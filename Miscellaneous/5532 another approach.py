"""
https://www.acmicpc.net/problem/5532 (방학 숙제)

Mathematics
Arithmetic
"""

from math import ceil
import sys

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

math = ceil(B / D)
language = ceil(A / C)

print(L - max(math, language))
