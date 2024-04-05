"""
https://www.acmicpc.net/problem/10026 (적록색약)

Graph Theory
Graph Traversal
Breadth-first Search
Depth-first Search

Solved with DFS
"""

import copy
import sys
sys.setrecursionlimit(int(1e5))


def dfs_abnormal(x, y, selected_color):
    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if abnormal_graph[x][y] != selected_color:
        return
    
    if not visited_abnormal[x][y]:
        visited_abnormal[x][y] = True
        dfs_abnormal(x-1, y, selected_color)
        dfs_abnormal(x+1, y, selected_color)
        dfs_abnormal(x, y-1, selected_color)
        dfs_abnormal(x, y+1, selected_color)
        return True


def dfs_normal(x, y, selected_color):
    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if original_graph[x][y] != selected_color:
        return

    if not visited_normal[x][y]:
        visited_normal[x][y] = True
        dfs_normal(x-1, y, selected_color)
        dfs_normal(x+1, y, selected_color)
        dfs_normal(x, y-1, selected_color)
        dfs_normal(x, y+1, selected_color)
        return True
    
    
N = int(sys.stdin.readline())
original_graph = []
visited_abnormal = [[False]*N for _ in range(N)]
visited_normal = [[False]*N for _ in range(N)]

for _ in range(N):
    original_graph.append(list(sys.stdin.readline().rstrip()))


abnormal_graph = copy.deepcopy(original_graph)

for x in range(N):
    for y in range(N):
        if abnormal_graph[x][y] in {"R", "G"}:
            abnormal_graph[x][y] = "R"

abnormal_cnt = 0

for x in range(N):
    for y in range(N):
        if not visited_abnormal[x][y] and dfs_abnormal(x, y, abnormal_graph[x][y]):
            abnormal_cnt += 1


normal_cnt = 0

for x in range(N):
    for y in range(N):
        if not visited_normal[x][y] and dfs_normal(x, y, original_graph[x][y]):
            normal_cnt += 1


print(normal_cnt, abnormal_cnt)
