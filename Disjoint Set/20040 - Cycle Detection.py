"""
https://www.acmicpc.net/problem/20040 (사이클 게임)

Data Structures
Disjoint Set
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

n, m = map(int, sys.stdin.readline().split())
parent = list(range(n))

for round in range(m):
    a, b = map(int, sys.stdin.readline().split())
    
    if find_parent(parent, a) == find_parent(parent, b):
        print(round+1)
        sys.exit()
    else:
        union_parent(parent, a, b)

print(0)
