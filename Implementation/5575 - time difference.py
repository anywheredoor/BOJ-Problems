"""
https://www.acmicpc.net/problem/5575 (타임 카드)

Mathematics
Implementation
Arithmetic
"""

import sys

for _ in range(3):
    start_h, start_m, start_s, end_h, end_m, end_s = map(int, sys.stdin.readline().split())
    
    start = start_h * 3600 + start_m * 60 + start_s
    end = end_h * 3600 + end_m * 60 + end_s
    
    total_seconds = end - start

    h = total_seconds // 3600
    m = total_seconds % 3600 // 60
    s = total_seconds % 3600 % 60

    print(h, m, s)
