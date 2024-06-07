"""
https://www.acmicpc.net/problem/4562 (No Brainer)

Implementation
"""
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    
    if x < y:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")
