"""
https://www.acmicpc.net/problem/11403 (경로 찾기)

Graph Theory
Graph Traversal
Shortest Path
Floyd–warshall

Solved with Floyd–warshall
"""

import sys

N = int(sys.stdin.readline())
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

for row in graph:
    print(*row, sep=" ")
