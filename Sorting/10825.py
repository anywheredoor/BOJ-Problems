"""
https://www.acmicpc.net/problem/10825 (국영수)

Sorting

page 550
"""

import sys

N = int(sys.stdin.readline())
data = []

for _ in range(N):
    name, a, b, c = sys.stdin.readline().split()
    data.append((name, int(a), int(b), int(c)))

data.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for info in data:
    print(info[0])
