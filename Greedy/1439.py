"""
https://www.acmicpc.net/problem/1439 (뒤집기)

Greedy
String
"""

import sys

S = sys.stdin.readline().rstrip()

my_dict = {"0":0, "1":0}
my_dict[S[0]] += 1
last = S[0]

for i in range(1, len(S)):
    if S[i] != last:
        my_dict[S[i]] += 1
        last = S[i]

print(min(my_dict["0"], my_dict["1"]))
