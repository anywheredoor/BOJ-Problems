"""
https://www.acmicpc.net/problem/6749 (Next in line)

Mathematics
Implementation
"""

import sys

Y = int(sys.stdin.readline())
M = int(sys.stdin.readline())

diff = M - Y

O = M + diff

print(O)
