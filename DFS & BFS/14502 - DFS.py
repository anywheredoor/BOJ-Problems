"""
https://www.acmicpc.net/submit/14502 (연구소)

Implementation
Graph Theory
Bruteforcing
Graph Traversal
Breadth-first Search

Solved with DFS
"""


from itertools import combinations
import copy
import sys


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return

    if graph[x][y] == 1:
        return

    graph[x][y] = 1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)


N, M = map(int, sys.stdin.readline().split())
graph = []
empty = []
virus = []
safe = 0


for idx1, _ in enumerate(range(N)):
    row = list(map(int, sys.stdin.readline().split()))
    
    for idx2, info in enumerate(row):
        if info == 0:
            empty.append((idx1, idx2))
        if info == 2:
            virus.append((idx1, idx2))
    
    graph.append(row)


original_graph = copy.deepcopy(graph)


for c1, c2, c3 in combinations(empty, 3):
    graph = copy.deepcopy(original_graph)
    
    x1, y1 = c1
    x2, y2 = c2
    x3, y3 = c3

    graph[x1][y1] = 1
    graph[x2][y2] = 1
    graph[x3][y3] = 1

    for c in virus:
        x, y = c
        dfs(x, y)

    cnt = 0
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    
    safe = max(safe, cnt)

    graph[x1][y1] = 0
    graph[x2][y2] = 0
    graph[x3][y3] = 0


print(safe)
