"""
https://www.acmicpc.net/problem/13136 (Do Not Touch Anything)

Mathematics
Arithmetic
"""
R, C, N = map(int, input().split())

if R % N == 0:
    n1 = R // N
else:
    n1 = R // N + 1

if C % N == 0:
    n2 = C // N
else:
    n2 = C // N + 1

print(n1 * n2)
