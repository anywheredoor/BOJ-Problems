"""
https://www.acmicpc.net/problem/2845 (파티가 끝나고 난 뒤)

Mathematics
Implementation
Arithmetic
"""

L, P = map(int, input().split())
newspaper = list(map(int, input().split()))

total = L * P

for i in range(5):
    newspaper[i] -= total

print(*newspaper, sep=" ")
