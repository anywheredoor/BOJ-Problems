"""
https://www.acmicpc.net/problem/10815 (숫자 카드)

Data Structures
Sorting
Binary Search
Set / Map By Hashing

Solved with Binary Search
"""

import sys

N = int(sys.stdin.readline())
cards = sorted(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

start, end = 0, len(cards)-1


def binary_search(number, start, end):
    while start <= end:
        mid = (start + end) // 2

        if cards[mid] == number:
            return True
        elif cards[mid] < number:
            start = mid + 1
        else:
            end = mid - 1

    return False


for number in numbers:
    if binary_search(number, start, end):
        print(1, end=" ")
    else:
        print(0, end=" ")
