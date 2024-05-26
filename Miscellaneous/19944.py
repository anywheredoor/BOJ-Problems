"""
https://www.acmicpc.net/problem/19944 (뉴비의 기준은 뭘까?)

Implementation
"""
N, M = map(int, input().split())

if M <= 2:
    print("NEWBIE!")
elif 2 < M <= N:
    print("OLDBIE!")
else:
    print("TLE!")
