"""
https://www.acmicpc.net/problem/20499 (Darius님 한타 안 함?)

Mathematics
Arithmetic
"""

import sys

K, D, A = map(int, sys.stdin.readline().split("/"))

if K + A < D or D == 0:
    print("hasu")
else:
    print("gosu")
