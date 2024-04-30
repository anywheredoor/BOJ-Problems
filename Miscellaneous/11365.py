"""
https://www.acmicpc.net/problem/11365 (!밀비 급일)

Implementation
String
"""

import sys

while True:
    key = sys.stdin.readline().rstrip()

    if key == "END":
        sys.exit()
    else:
        print(key[::-1])
