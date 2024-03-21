"""
https://www.acmicpc.net/problem/11399 (ATM)

Greedy
Sorting
"""

import sys

N = int(sys.stdin.readline())
queue = sorted(map(int, sys.stdin.readline().split()))
acc_list = [0]

for i in range(N):
    acc_list.append(acc_list[i] + queue[i])

print(sum(acc_list))
