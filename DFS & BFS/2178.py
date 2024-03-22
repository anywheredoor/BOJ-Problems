"""
https://www.acmicpc.net/problem/2178 (미로 탐색)

Graph Theory
Graph Traversal
Breadth-first Search

Solved with BFS
"""

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs()
print(graph[-1][-1])
