"""
https://www.acmicpc.net/problem/15726 (이칙연산)

Mathematics
Arithmetic
"""
data = list(map(int, input().split()))

outcome_1 = data[0] * data[1] / data[2]
outcome_2 = data[0] / data[1] * data[2]

print(int(max(outcome_1, outcome_2)))
