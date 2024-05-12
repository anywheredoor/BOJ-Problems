"""
https://www.acmicpc.net/problem/11945 (뜨거운 붕어빵)

Implementation
String
"""

import sys

N, M = map(int, sys.stdin.readline().split())
shape = []

for _ in range(N):
    shape.append(list(sys.stdin.readline().rstrip()))

for row in shape:
    print("".join(row[::-1]))
