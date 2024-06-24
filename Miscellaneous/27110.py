"""
https://www.acmicpc.net/problem/27110 (특식 배부)

Mathematics
Arithmetic
"""
N = int(input())
A, B, C = map(int, input().split())

if A > N:
    A = N

if B > N:
    B = N

if C > N:
    C = N

print(A + B + C)
