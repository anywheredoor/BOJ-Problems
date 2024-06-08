"""
https://www.acmicpc.net/problem/25191 (치킨댄스를 추는 곰곰이를 본 임스)

Mathematics
Arithmetic
"""

N = int(input())
A, B = map(int, input().split())

total = A // 2 + B

if total > N:
    total = N

print(total)
