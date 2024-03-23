"""
https://www.acmicpc.net/problem/2805 (나무 자르기)

Binary Search
Parametric Search

Solved with Parametric Search
"""

import sys

N, M = map(int, sys.stdin.readline().split())
tree_heights = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree_heights)
ans = 0

while start <= end:
    mid = (start + end) // 2
    
    total = 0

    for height in tree_heights:
        if height > mid:
            total += height - mid

    if total < M:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1
        
print(ans)
