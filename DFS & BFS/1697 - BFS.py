"""
https://www.acmicpc.net/problem/1697 (숨바꼭질)

Graph Theory
Graph Traversal
Breadth-first Search

Solved with BFS
"""


import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

if N == K:
    print(0)
    sys.exit()

if N > K:
    print(N - K)
    sys.exit()

graph = [0] * 200001
visited = [False] * 200001
dx = [-1, 1, 2]


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        x = queue.popleft()

        for i in range(3):
            nx = x * 2 if i == 2 else x + dx[i]

            if 0 <= nx <= 200000 and not visited[nx]:
                graph[nx] = graph[x] + 1
                queue.append(nx)
                visited[nx] = True

            if nx == K:
                print(graph[nx])
                sys.exit()
        

bfs(N)
