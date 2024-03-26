"""
https://www.acmicpc.net/problem/1654 (랜선 자르기)

Binary Search
Parametric Search

Solved with Parametric Search
"""

import sys

K, N = map(int, sys.stdin.readline().split())
lines = []

for _ in range(K):
    lines.append(int(sys.stdin.readline()))

start = 1
end = max(lines)

while start <= end:
    mid = (start + end) // 2

    cnt = 0

    for line in lines:
        cnt += line // mid

    if cnt < N:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)
