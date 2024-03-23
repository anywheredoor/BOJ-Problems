"""
https://www.acmicpc.net/problem/11047 (동전 0)

Greedy
"""

import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
ans = 0

for _ in range(N):
    coin = int(sys.stdin.readline())

    if coin <= K:
        coins.append(coin)

while K:
    ans += K // coins[-1]
    K %= coins[-1]
    coins.pop()

print(ans)
