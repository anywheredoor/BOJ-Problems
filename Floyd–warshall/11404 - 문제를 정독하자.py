"""
https://www.acmicpc.net/problem/11404 (플로이드)

Graph Theory
Shortest Path
Floyd–warshall

Solved with Floyd–warshall

* 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
* 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
"""

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for x in range(1, n+1):
    graph[x][x] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            graph[a][b] = 0

for row in graph[1:]:
    print(*row[1:], sep=" ")
