"""
https://www.acmicpc.net/problem/2775 (부녀회장이 될테야)

Mathematics
Implementation
Dynamic Programming
"""

import sys

dp = [[0]*(15) for _ in range(15)]

for i in range(1, 15):
    dp[0][i] = i

for floor in range(1, 15):
    for room in range(1, 15):
        dp[floor][room] = dp[floor][room-1] + dp[floor-1][room]


T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(dp[k][n])
