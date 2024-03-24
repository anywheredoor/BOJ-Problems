"""
https://www.acmicpc.net/problem/2839 (설탕 배달)

Mathematics
Dynamic Programming
Greedy

Solved with Dynamic Programming
"""

import sys

N = int(sys.stdin.readline())
dp = [-1]*(5001)
dp[3] = 1
dp[5] = 1

for i in range(6, N+1):
    if dp[i-3] != -1:
        dp[i] = dp[i-3] + 1
    if dp[i-5] != -1:
        dp[i] = dp[i-5] + 1

print(dp[N])
