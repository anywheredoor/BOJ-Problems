"""
https://www.acmicpc.net/problem/10816 (숫자 카드 2)

Data Structures
Sorting
Binary Search
Set / Map By Hashing

Solved with Binary Search - count_by_range
"""

import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())
card_list = sorted(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

def count_by_range(array, left_val, right_val):
    right_idx = bisect_right(array, right_val)
    left_idx = bisect_left(array, left_val)
    return right_idx - left_idx

for target in targets:
    ans = count_by_range(card_list, target, target)
    print(ans, end=" ")
