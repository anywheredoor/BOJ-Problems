"""
https://www.acmicpc.net/problem/17356 (욱 제)

Mathematics
Arithmetic
"""
A, B = map(int, input().split())

M = (B - A) / 400
ans = 1 / (1 + (10 ** M))

print(ans)
