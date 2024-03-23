"""
https://www.acmicpc.net/problem/1920 (수 찾기)

Data Structures
Sorting
Binary Search

Solved with Binary Search - Recursive Method
"""


import sys

N = int(sys.stdin.readline())
array = sorted(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))


def binary_search(array, target, start, end):
    if start > end:
        return False

    mid = (start + end) // 2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


for target in targets:
    if binary_search(array, target, 0, N-1):
        print(1)
    else:
        print(0)
