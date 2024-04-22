"""
https://www.acmicpc.net/problem/1715 (카드 정렬하기)

Data Structures
Greedy
Priority Queue
"""

import heapq

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)
