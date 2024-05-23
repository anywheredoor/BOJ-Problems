"""
https://www.acmicpc.net/problem/17362 (수학은 체육과목 입니다 2)

Mathematics
Arithmetic
"""
n = int(input())

my_list = [1, 2, 3, 4, 5, 4, 3, 2]

print(my_list[n % 8 - 1])
