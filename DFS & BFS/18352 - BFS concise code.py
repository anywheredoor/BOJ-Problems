"""
https://www.acmicpc.net/problem/18352 (특정 거리의 도시 찾기)

Graph Theory
Graph Traversal
Breadth-first Search
Dijkstra's
Shortest Path

Solved with BFS
"""

import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
distance = [-1] * (N+1)
exist = False

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

def bfs(start):
    queue = deque()
    queue.append(start)
    distance[start] = 0

    while queue:
        now = queue.popleft()

        for node in graph[now]:
            if distance[node] == -1:
                queue.append(node)
                distance[node] = distance[now] + 1

bfs(X)

for i in range(1, N+1):
    if distance[i] == K:
        exist = True
        print(i)

if not exist:
    print(-1)
