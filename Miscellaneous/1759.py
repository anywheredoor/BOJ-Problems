"""
https://www.acmicpc.net/problem/1759 (암호 만들기)

Mathematics
Bruteforcing
Combinatorics
Backtracking
"""

import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
letters = sys.stdin.readline().split()
satisfied_list = []

for comb in combinations(letters, L):
    cnt_v = 0
    cnt_c = 0
    for letter in comb:
        if letter in {'a', 'e', 'i', 'o', 'u'}:
            cnt_v += 1
        else:
            cnt_c += 1
        if cnt_v >= 1 and cnt_c >= 2:
            satisfied_list.append("".join(sorted(comb)))
            break

print(*sorted(satisfied_list), sep="\n")
