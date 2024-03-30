"""
https://www.acmicpc.net/problem/1976 (여행 가자)

Data Structures
Graph Theory
Graph Traversal
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

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = list(range(N+1))

for idx1 in range(N):
    my_list = list(map(int, sys.stdin.readline().split()))
    for idx2, info in enumerate(my_list):
        if info:
            union_parent(parent, idx1+1, idx2+1)

plans = list(map(int, sys.stdin.readline().split()))

for i in range(1, M):
    if find_parent(parent, plans[i-1]) == find_parent(parent, plans[i]):
        continue
    else:
        print("NO")
        sys.exit()

print("YES")
