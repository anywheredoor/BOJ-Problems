"""
https://www.acmicpc.net/problem/1647 (도시 분할 계획)

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

N, M = map(int, sys.stdin.readline().split())

parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i

edges = []

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((C, A, B))

edges.sort()

total = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total += cost
        last = cost

print(total - last)
