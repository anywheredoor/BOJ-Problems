"""
https://www.acmicpc.net/problem/19698 (헛간 청약)

Mathematics
Arithmetic
"""
N, W, H, L = map(int, input().split())

print(min(((W // L) * (H // L)), N))
