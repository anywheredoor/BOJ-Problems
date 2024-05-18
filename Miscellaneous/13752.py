"""
https://www.acmicpc.net/problem/13752 (히스토그램)

Implementation
"""

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    k = int(sys.stdin.readline())
    print("=" * k)
