"""
https://www.acmicpc.net/problem/11943 (파일 옮기기)

Mathematics
Implementation
"""

import sys

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

outcomes = []

outcomes.append(A + D)
outcomes.append(C + B)

print(min(outcomes))
