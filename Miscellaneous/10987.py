"""
https://www.acmicpc.net/problem/10987 (모음의 개수)

Implementation
String
"""

import sys

my_set = {"a", "e", "i", "o", "u"}
cnt = 0

word = sys.stdin.readline()

for c in word:
    if c in my_set:
        cnt += 1

print(cnt)
