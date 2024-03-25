"""
https://www.acmicpc.net/problem/1931 (회의실 배정)

Greedy
Sorting
"""

import sys

N = int(sys.stdin.readline())
meetings = []

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    meetings.append((s, e))

meetings.sort(key=lambda x: (x[1], x[0])) # Important --> key에 튜플로 여러 인자를 주면 해당 인자의 순서대로 정렬
"""
2
2 2
1 2

2
1 2
2 2

different result for this problem!
"""

current_time = 0
cnt = 0

for start, end in meetings:
    if start >= current_time:
        current_time = end
        cnt += 1

print(cnt)
