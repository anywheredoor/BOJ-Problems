"""
https://www.acmicpc.net/problem/11726 (2×n 타일링)

Dynamic Programming
"""

import sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)
dp[0] = 1 # to prevent index error
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] %= 10007

print(dp[n] % 10007)
