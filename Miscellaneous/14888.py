"""
https://www.acmicpc.net/problem/14888 (연산자 끼워넣기)

Bruteforcing
Backtracking
"""

import sys
from itertools import permutations

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
operator_count = list(map(int, sys.stdin.readline().split()))
operator = ("+", "-", "*", "//")
my_list = []
answer = []

for n, o in zip(operator_count, operator):
    for _ in range(n):
        my_list.append(o)

for case in permutations(my_list):
    result = sequence[0]
    for num, oper in zip(sequence[1:], case):
        if oper == "+":
            result += num
        elif oper == "-":
            result -= num
        elif oper == "*":
            result *= num
        else:
            if result < 0:
                result = -result
                result //= num
                result = -result
            else:
                result //= num
    answer.append(result)

print(max(answer))
print(min(answer))
