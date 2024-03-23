"""
https://www.acmicpc.net/problem/1012 (유기농 배추)

Graph Theory
Graph Traversal
Breadth-first Search
Depth-first Search

Solved with DFS
"""

import sys
sys.setrecursionlimit(int(1e9))


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return

    if not visited[x][y] and graph[x][y]:
        visited[x][y] = True
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True


T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    
    ans = 0
    
    for x in range(N):
        for y in range(M):
            if dfs(x, y):
                ans += 1
    
    print(ans)
