"""
https://www.acmicpc.net/problem/2003 (수들의 합 2)

Bruteforcing
Prefix Sum
Two-pointer

Solved with Two-pointer
"""

import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

end = 0
interval_sum = 0
cnt = 0

for start in range(N):
    while interval_sum < M and end < N:
        interval_sum += array[end]
        end += 1

    if interval_sum == M:
        cnt += 1

    interval_sum -= array[start]

print(cnt)
