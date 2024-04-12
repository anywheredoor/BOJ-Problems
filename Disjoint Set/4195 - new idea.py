"""
https://www.acmicpc.net/problem/4195 (친구 네트워크)

Data Structures
Set / Map By Hashing
Disjoint Set

Solved with Disjoint Set
"""

import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        parent[b] = a
        count[a] += count[b]

    print(count[a])


T = int(sys.stdin.readline())

for _ in range(T):
    F = int(sys.stdin.readline())
    
    parent = {}
    count = {}
    
    for _ in range(F):
        a, b = sys.stdin.readline().split()
    
        if a not in parent:
            parent[a] = a
            count[a] = 1
    
        if b not in parent:
            parent[b] = b
            count[b] = 1
    
        union_parent(parent, a, b)
