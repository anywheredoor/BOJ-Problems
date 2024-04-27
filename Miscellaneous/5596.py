"""
https://www.acmicpc.net/problem/5596 (시험 점수)

Mathematics
Implementation
Arithmetic
"""

import sys

S = sum(list(map(int, sys.stdin.readline().split())))
T = sum(list(map(int, sys.stdin.readline().split())))

if S >= T:
    print(S)
else:
    print(T)
