"""
https://www.acmicpc.net/problem/5717 (상근이의 친구들)

Mathematics
Arithmetic
"""

import sys

while True:
    total = sum(map(int, sys.stdin.readline().split()))

    if total == 0:
        sys.exit()
    else:
        print(total)
