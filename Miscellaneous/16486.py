"""
https://www.acmicpc.net/problem/16486 (운동장 한 바퀴)

Mathematics
Geometry
"""

import sys

d1 = int(sys.stdin.readline())
d2 = int(sys.stdin.readline())

circumference = (2 * d1) + (2 * 3.141592 * d2)

print(circumference)
