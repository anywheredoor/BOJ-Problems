"""
https://www.acmicpc.net/problem/3190 (뱀)

Implementation
Data Structures
Simulation
Deque
Queue
"""

import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
data = [[0]*(N+1) for _ in range(N+1)]
info = []

for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    data[r][c] = 1

L = int(sys.stdin.readline())
for _ in range(L):
    X, C = sys.stdin.readline().split()
    info.append((int(X), C))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
   
    while True: 
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= N and 1 <= ny <= N and data[nx][ny] != 2:
            
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
    
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))

        else:
            time += 1
            break
    
        x, y = nx, ny
        time += 1
        
        if index < L and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1

    return time

print(simulate())
