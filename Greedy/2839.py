"""
https://www.acmicpc.net/problem/2839 (설탕 배달)

Mathematics
Dynamic Programming
Greedy

Solved with Greedy

https://velog.io/@mini-dora/파이썬-백준-2839번-설탕-배달
"""

import sys

N = int(sys.stdin.readline())

if N % 5 == 0:
    print(N//5)
else:
    cnt = 0
    
    while N >= 3:
        N -= 3
        cnt += 1

        if N == 0:
            print(cnt)
            break

        if N % 5 == 0:
            print(cnt + N//5)
            break
    else:
        print(-1)
