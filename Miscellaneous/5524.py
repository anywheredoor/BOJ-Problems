"""
https://www.acmicpc.net/problem/5524 (입실 관리)

String
"""

import sys

N = int(sys.stdin.readline())
for _ in range(N):
    name = sys.stdin.readline().rstrip().lower()
    print(name)
