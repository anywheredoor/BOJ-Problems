"""
https://www.acmicpc.net/problem/2839 (설탕 배달)

Mathematics
Dynamic Programming
Greedy

Solved with Dynamic Programming
"""

import sys

N = int(sys.stdin.readline())

dp = [5001]*(N+1)
dp[0] = 0

bags = (3, 5)

for i in bags:
    for j in range(i, N+1):
        dp[j] = min(dp[j], dp[j - i] + 1)

print(dp[N] if dp[N]!= 5001 else -1)
