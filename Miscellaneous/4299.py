"""
https://www.acmicpc.net/problem/4299 (AFC 윔블던)

Mathematics
Arithmetic
"""

import sys

total, difference = map(int, sys.stdin.readline().split())

s1 = (total + difference) // 2
s2 = (total - difference) // 2

if total < difference:
    print(-1)
else:
    if s1 + s2 == total and s1 - s2 == difference:
        print(s1, s2)
    else:
        print(-1)
