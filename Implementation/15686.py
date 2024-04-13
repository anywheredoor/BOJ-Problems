"""
https://www.acmicpc.net/problem/15686 (치킨 배달)

Implementation
Bruteforcing
Backtracking
"""

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
graph = []
house = []
chicken = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i+1, j+1))
        if graph[i][j] == 2:
            chicken.append((i+1, j+1))

answer = int(1e9)

for comb in combinations(chicken, M):
    distance = []
    
    for house_coord in house:
        minimum = int(1e9)
        for chicken_coord in comb:
            r1, c1 = house_coord
            r2, c2 = chicken_coord
            minimum = min(minimum, abs(r1-r2) + abs(c1-c2))
        distance.append(minimum)

    answer = min(answer, sum(distance))

print(answer)
