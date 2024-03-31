"""
https://www.acmicpc.net/problem/1043 (거짓말)

Data Structures
Graph Theory
Graph Traversal
Disjoint Set

Didn't use Disjoint Set

https://ku-hug.tistory.com/148
"""

import sys

N, M = map(int, sys.stdin.readline().split())
truth = set(map(int, sys.stdin.readline().split()[1:]))
party_list = []
cnt = 0

for _ in range(M):
    party_list.append(set(map(int, sys.stdin.readline().split()[1:])))

for _ in range(M):
    for party in party_list:
        if party & truth:
            truth.update(party)

for party in party_list:
    if party & truth:
        continue
    else:
        cnt += 1

print(cnt)
