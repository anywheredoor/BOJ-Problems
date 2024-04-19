"""
https://www.acmicpc.net/problem/5585 (거스름돈)

Greedy
"""

import sys

cost = 1000 - int(sys.stdin.readline())
change = (500, 100, 50, 10, 5, 1)
cnt = 0

for amount in change:
    if amount <= cost:
        cnt += cost // amount
        cost %= amount

print(cnt)
