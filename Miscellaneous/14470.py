"""
https://www.acmicpc.net/problem/14470 (전자레인지)

Mathematics
Implementation
Arithmetic
Simulation
"""
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

frozen = True
time = 0

while A < B:
    if A < 0:
        A += 1
        time += C
    elif A == 0 and frozen:
        frozen = False
        time += D
    else:
        A += 1
        time += E

print(time)
