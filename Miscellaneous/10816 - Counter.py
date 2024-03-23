"""
https://www.acmicpc.net/problem/10816 (숫자 카드 2)

Data Structures
Sorting
Binary Search
Set / Map By Hashing

Solved with Counter
"""

import sys
from collections import Counter

N = sys.stdin.readline()
counter = Counter(sys.stdin.readline().split())
M = sys.stdin.readline()
targets = sys.stdin.readline().split()

for target in targets:
    print(counter[target], end=" ")
