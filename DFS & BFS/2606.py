"""
https://www.acmicpc.net/problem/2606 (바이러스)

Graph Theory
Graph Traversal
Breadth-first Search
Depth-first Search

Solved with DFS & Adjacency Matrix
"""

import sys

n = int(sys.stdin.readline())
edges = int(sys.stdin.readline())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(edges):
    c1, c2 = map(int, sys.stdin.readline().split())
    graph[c1][c2] = graph[c2][c1] = 1

def dfs(v):
    visited[v] = True
    
    for i in range(1, n+1):
        if graph[v][i] and not visited[i]:
            dfs(i)

dfs(1)

print(sum(visited)-1)
