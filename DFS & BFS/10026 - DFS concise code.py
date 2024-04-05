"""
https://www.acmicpc.net/problem/10026 (적록색약)

Graph Theory
Graph Traversal
Breadth-first Search
Depth-first Search

Solved with DFS
"""

import sys
sys.setrecursionlimit(int(1e4))


def dfs(x, y, selected_color):
    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if graph[x][y] != selected_color:
        return
    
    if not visited[x][y]:
        visited[x][y] = True
        dfs(x-1, y, selected_color)
        dfs(x+1, y, selected_color)
        dfs(x, y-1, selected_color)
        dfs(x, y+1, selected_color)
        return True


# input & initialization
N = int(sys.stdin.readline())
graph = []
visited = [[False]*N for _ in range(N)]

for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))


# normal
normal_cnt = 0

for x in range(N):
    for y in range(N):
        if not visited[x][y] and dfs(x, y, graph[x][y]):
            normal_cnt += 1


# abnormal
for x in range(N):
    for y in range(N):
        if graph[x][y] == "R":
            graph[x][y] = "G"

visited = [[False]*N for _ in range(N)]
abnormal_cnt = 0

for x in range(N):
    for y in range(N):
        if not visited[x][y] and dfs(x, y, graph[x][y]):
            abnormal_cnt += 1
            

print(normal_cnt, abnormal_cnt)
