"""
https://www.acmicpc.net/problem/25628 (햄버거 만들기)

Mathematics
Arithmetic
"""
A, B = map(int, input().split())

ans = min(A // 2, B)

print(ans)
