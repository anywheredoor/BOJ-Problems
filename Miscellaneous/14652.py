"""
https://www.acmicpc.net/problem/14652 (나는 행복합니다~)

Mathematics
Arithmetic
"""

import sys

N, M, K = map(int, sys.stdin.readline().split())

n = K // M
m = K % M

print(n, m)
