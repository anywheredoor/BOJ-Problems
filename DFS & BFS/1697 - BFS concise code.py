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
graph = [0] * 200001


def bfs(start):
    queue = deque()
    queue.append(start)
    
    while queue:
        x = queue.popleft()

        # N == K right from the beginning
        if x == K:
            print(graph[K])
            sys.exit()
        
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= 200000 and not graph[nx]:
                graph[nx] = graph[x] + 1
                queue.append(nx)
                
                
bfs(N)
