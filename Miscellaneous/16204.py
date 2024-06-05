"""
https://www.acmicpc.net/problem/16204 (카드 뽑기)

Mathematics
Implementation
Arithmetic
"""
N, M, K = map(int, input().split())

O = M
X = N - M

if O > K:
    O = K

if X > (N - K):
    X = N - K

print(O + X)
