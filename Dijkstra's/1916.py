"""
https://www.acmicpc.net/problem/1916 (최소비용 구하기)

Graph Theory
Dijkstra's
Shortest Path
"""

import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

start, end = map(int, sys.stdin.readline().split())

INF = int(1e9)
distance = [INF] * (n+1)

def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0

    while h:
        dist, now = heapq.heappop(h)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))

dijkstra(start)

print(distance[end])
