"""
https://www.acmicpc.net/problem/17388 (와글와글 숭고한)

Implementation
"""

import sys

universities = list(map(int, sys.stdin.readline().split()))

if sum(universities) >= 100:
    print("OK")
else:
    lowest = min(universities)
    lowest_idx = universities.index(lowest)

    my_dict = {0: "Soongsil",
               1: "Korea",
               2: "Hanyang"}

    print(my_dict[lowest_idx])
