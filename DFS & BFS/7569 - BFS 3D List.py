"""
https://www.acmicpc.net/problem/7569 (토마토)

Graph Theory
Graph Traversal
Breadth-first Search

Solved with BFS
"""

from collections import deque
import sys


M, N, H = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(H)]
tomato = []

for height in range(H):
    for row in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        
        for col, info in enumerate(line):
            if info == 1:
                tomato.append((height, row, col))
        
        graph[height].append(line)
        

def bfs():
    queue = deque()

    for coord in tomato:
        z, x, y = coord
        queue.append((z, x, y))
    
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))

    day = 1
    
    for height in range(H):
        for row in range(N):
            for col in range(M):
                if graph[height][row][col] == 0:
                    print(-1)
                    sys.exit()
                day = max(day, graph[height][row][col])

    print(day-1)


bfs()
