"""
https://www.acmicpc.net/problem/11549 (Identifying tea)

Implementation
"""
from collections import Counter

T = int(input())
counter = Counter(map(int, input().split()))

print(counter[T])
