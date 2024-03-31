"""
https://www.acmicpc.net/problem/1005 (ACM Craft)

Dynamic Programming
Graph Theory
Topological Sorting
Directed Acyclic Graph
"""

from collections import deque
import copy
import sys


def topology_sort():
    q = deque()
    finished = copy.deepcopy(time)
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
    
        for i in graph[now]:
            indegree[i] -= 1
            finished[i] = max(finished[i], finished[now] + time[i])
    
            if indegree[i] == 0:
                q.append(i)
    
    print(finished[W])


T = int(sys.stdin.readline())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    time = [0] + list(map(int, sys.stdin.readline().split()))
    
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[X].append(Y)
        indegree[Y] += 1
    
    W = int(sys.stdin.readline())
    
    topology_sort()
