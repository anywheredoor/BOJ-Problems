"""
https://www.acmicpc.net/problem/2839 (설탕 배달)

Mathematics
Dynamic Programming
Greedy

Solved with Dynamic Programming
"""

import sys

N = int(sys.stdin.readline())

dp = [5001]*5001
dp[3] = dp[5] = 1

for i in range(6, 5001):
    dp[i] = min(dp[i], dp[i-3]+1, dp[i-5]+1)

print(dp[N] if dp[N]!=5001 else -1)
