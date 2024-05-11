"""
https://www.acmicpc.net/problem/4470 (줄번호)

Implementation
String
"""

import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    line = sys.stdin.readline().rstrip()
    print(f"{i}. {line}")
