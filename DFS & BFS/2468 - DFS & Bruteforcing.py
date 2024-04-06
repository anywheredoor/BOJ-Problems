"""
https://www.acmicpc.net/problem/2468 (안전 영역)

Graph Theory
Bruteforcing
Graph Traversal
Breadth-first Search
Depth-first Search

Solved with DFS
"""

import sys
sys.setrecursionlimit(int(1e4))

N = int(sys.stdin.readline())
graph = []
highest = 1
ans = 0

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    highest = max(highest, max(row))
    graph.append(row)


def dfs(x, y, rain):
    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if not visited[x][y] and graph[x][y] > rain:
        visited[x][y] = True
        dfs(x-1, y, rain)
        dfs(x+1, y, rain)
        dfs(x, y-1, rain)
        dfs(x, y+1, rain)
        return True
    

# highest + 1 -> there is no safe area, thus 0.
for rain in range(highest):
    visited = [[False]*N for _ in range(N)]
    safe = 0
    
    for x in range(N):
        for y in range(N):
            if dfs(x, y, rain):
                safe += 1

    ans = max(ans, safe)


print(ans)
