"""
https://www.acmicpc.net/problem/14501 (퇴사)

Dynamic Programming
Bruteforcing
"""

import sys

T = [0]
P = [0]

N = int(sys.stdin.readline())
for _ in range(N):
    Ti, Pi = map(int, sys.stdin.readline().split())
    T.append(Ti)
    P.append(Pi)

dp = [0]*(N+1)

for i in range(1, N+1):
    for j in range(i):
        if j + (T[j] - 1) < i and i + (T[i] - 1) <= N:
            dp[i] = max(dp[i], dp[j] + P[i])

print(max(dp))
