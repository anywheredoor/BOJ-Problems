"""
https://www.acmicpc.net/problem/2667 (단지번호붙이기)

Graph Theory
Graph Traversal
Breadth-first Search
Depth-first Search

Solved with DFS
"""

import sys

N = int(sys.stdin.readline())
graph = []
visited = [[False]*N for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


def dfs(x, y):
    global cnt
    
    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if not visited[x][y] and graph[x][y]:
        visited[x][y] = True
        cnt += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
        

blocks = 0
cnt_list = []

for x in range(N):
    for y in range(N):
        cnt = 0
        if dfs(x, y):
            blocks += 1
            cnt_list.append(cnt)

cnt_list.sort()

print(blocks)
print(*cnt_list, sep="\n")
