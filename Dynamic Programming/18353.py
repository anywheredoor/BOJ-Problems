"""
https://www.acmicpc.net/problem/18353 (병사 배치하기)

Dynamic Programming
Longest Increasing Sequence In O(n Log N)
"""

import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if a[j] > a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
