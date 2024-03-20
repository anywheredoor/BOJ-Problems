"""
https://www.acmicpc.net/problem/1260 (DFS와 BFS)

Graph Theory
Graph Traversal
Breadth-first Search
Depth-first Search

Solved with Adjacency List
"""

import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for info in graph:
    info.sort()

def dfs(node):
    visited[node] = True
    
    print(node, end=" ")
    
    for adj in graph[node]:
        if not visited[adj]:
            dfs(adj)

def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = True

    while queue:
        node = queue.popleft()

        print(node, end=" ")
        
        for adj in graph[node]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True

dfs(V)
print()

visited = [False]*(N+1)
bfs(V)
