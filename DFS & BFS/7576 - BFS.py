"""
https://www.acmicpc.net/problem/7576 (토마토)

Graph Theory
Graph Traversal
Breadth-first Search

Solved with BFS
"""

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
graph = []
visited = [[False]*(M+1) for _ in range(N+1)]
queue = deque() 

for idx1, _ in enumerate(range(N)):
    row = list(map(int, sys.stdin.readline().split()))
    
    for idx2, info in enumerate(row):
        if info == 1:
            queue.append((idx1, idx2))
            visited[idx1][idx2] = True
            
    graph.append(row)


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


bfs()

day = 0

for x in range(N):
    for y in range(M):
        if graph[x][y] == 0:
            print(-1)
            sys.exit()

        day = max(day, graph[x][y])

print(day-1)
