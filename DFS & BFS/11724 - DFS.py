"""
https://www.acmicpc.net/problem/11724 (연결 요소의 개수)

Graph Theory
Graph Traversal
Breadth-first Search
Depth-first Search

Solved with DFS
"""

import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            dfs(i)

cnt = 0

for node in range(1, N+1):
    if not visited[node]:
        dfs(node)
        cnt += 1

print(cnt)
