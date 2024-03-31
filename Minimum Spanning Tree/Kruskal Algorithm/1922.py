"""
https://www.acmicpc.net/problem/1922 (네트워크 연결)

Graph Theory
Minimum Spanning Tree

Solved with Kruskal Algorithm
"""

import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = list(range(N+1))
edges = []
total = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total += cost

print(total)
