"""
https://www.acmicpc.net/problem/18406 (럭키 스트레이트)

Implementation
String
"""

import sys

my_list = list(map(int, sys.stdin.readline().rstrip()))

half = len(my_list) // 2

if sum(my_list[:half]) == sum(my_list[half:]):
    print("LUCKY")
else:
    print("READY")
