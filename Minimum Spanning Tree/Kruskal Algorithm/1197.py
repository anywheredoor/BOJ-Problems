"""
https://www.acmicpc.net/problem/1197 (최소 스패닝 트리)

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

V, E = map(int, sys.stdin.readline().split())
parent = list(range(V+1))
edges = []
total = 0

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((C, A, B))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total += cost

print(total)
