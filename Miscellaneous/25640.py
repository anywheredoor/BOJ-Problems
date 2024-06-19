"""
https://www.acmicpc.net/problem/25640 (MBTI)

Implementation
String
"""
import sys

MBTI = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())

cnt = 0

for _ in range(N):
    if sys.stdin.readline().rstrip() == MBTI:
        cnt += 1

print(cnt)
