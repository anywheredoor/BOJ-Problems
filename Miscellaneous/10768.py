"""
https://www.acmicpc.net/problem/10768 (특별한 날)

Implementation
"""

import sys

month = int(sys.stdin.readline())
day = int(sys.stdin.readline())

if month < 2 or (month <= 2 and day < 18):
    print("Before")
elif month == 2 and day == 18:
    print("Special")
else:
    print("After")
