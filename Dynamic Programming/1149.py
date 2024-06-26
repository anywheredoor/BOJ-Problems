"""
https://www.acmicpc.net/problem/1149 (RGB거리)

Dynamic Programming
"""

import sys

N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

for i in range(3):
    dp[0][i] = cost[0][i]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[-1]))
