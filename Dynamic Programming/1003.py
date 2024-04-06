"""
https://www.acmicpc.net/problem/1003 (피보나치 함수)

Dynamic Programming
"""

import sys

dp = [[0, 0]*(41) for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1

for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    print(dp[N][0], dp[N][1])
