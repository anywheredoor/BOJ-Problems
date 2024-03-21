"""
https://www.acmicpc.net/problem/11399 (ATM)

Greedy
Sorting
"""

import sys

N = int(sys.stdin.readline())
queue = sorted(map(int, sys.stdin.readline().split()))
ans = 0

for i in range(1, N+1):
    ans += sum(queue[:i])

print(ans)
