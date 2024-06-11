"""
https://www.acmicpc.net/problem/25377 (빵)

Implementation
"""
N = int(input())
time = 1001
possible = False

for _ in range(N):
    A, B = map(int, input().split())

    if A <= B:
        possible = True
        time = min(time, B)

if possible:
    print(time)
else:
    print(-1)
