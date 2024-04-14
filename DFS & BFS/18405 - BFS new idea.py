"""
https://www.acmicpc.net/problem/18405 (경쟁적 전염)

Implementation
Graph Theory
Graph Traversal
Breadth-first Search

Solved with BFS
"""

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
graph = []
virus = []
queue = deque()

for x in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for y in range(N):
        if graph[x][y]:
            virus.append((graph[x][y], x, y))

S, X, Y = map(int, sys.stdin.readline().split())

virus.sort()
for _, x, y in virus:
    queue.append((x, y))


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if not graph[nx][ny]:
                graph[nx][ny] = graph[x][y]
                next.append((nx, ny))


for _ in range(S):
    next = []
    bfs()
    for x, y in next:
        queue.append((x, y))

print(graph[X-1][Y-1])
