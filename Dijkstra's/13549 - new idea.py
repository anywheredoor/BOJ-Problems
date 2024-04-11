"""
https://www.acmicpc.net/problem/13549 (숨바꼭질 3)

Graph Theory
Graph Traversal
Breadth-first Search
Dijkstra's
Shortest Path
0-1 Bfs

Solved with Dijkstra's
"""

import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

INF = int(1e9)
distance = [INF] * 100001


def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0

    while h:
        dist, now = heapq.heappop(h)

        if distance[now] < dist:
            continue

        for n_dist, n_x in ((dist+1, now-1), (dist+1, now+1), (dist, 2*now)):
            if 0 <= n_x <= 100000 and distance[n_x] > n_dist:
                distance[n_x] = n_dist
                heapq.heappush(h, (n_dist, n_x))


dijkstra(N)
print(distance[K])
