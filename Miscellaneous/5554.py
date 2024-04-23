"""
https://www.acmicpc.net/problem/5554 (심부름 가는 길)

Mathematics
Implementation
Arithmetic
"""

import sys

total = 0

for _ in range(4):
    total += int(sys.stdin.readline())

print(total // 60)
print(total % 60)
