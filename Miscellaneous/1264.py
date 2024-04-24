"""
https://www.acmicpc.net/problem/1264 (모음의 개수)

Implementation
String
"""

import sys

v = {'a', 'e', 'i', 'o', 'u',
     'A', 'E', 'I', 'O', 'U'}

while True:
    s = list(sys.stdin.readline())

    if s[0] == "#":
        break
    
    cnt = 0
    
    for c in s:
        if c in v:
            cnt += 1

    print(cnt)
