"""
https://www.acmicpc.net/problem/2110 (공유기 설치)

Binary Search
Parametric Search
"""

import sys

N, C = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(N)]
house.sort()

start = 1
end = house[-1] - house[0]
ans = 0


def binary_search(start, end):
    global ans
    
    while start <= end:
        mid = (start + end) // 2
        now = house[0]
        cnt = 1
        
        for i in range(1, len(house)):
            if house[i] - now >= mid:
                cnt += 1
                now = house[i]

        if cnt >= C:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1


binary_search(start, end)
print(ans)
