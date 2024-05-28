"""
https://www.acmicpc.net/problem/14924 (폰 노이만과 파리)

Mathematics
Arithmetic
"""
S, T, D = map(int, input().split())

when = D // (2 * S)

print(when * T)
