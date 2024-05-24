"""
https://www.acmicpc.net/problem/13866 (팀 나누기)

Mathematics
Implementation
Arithmetic
"""
my_list = sorted(map(int, input().split()))

team_1 = my_list[0] + my_list[3]
team_2 = my_list[1] + my_list[2]

print(abs(team_1 - team_2))
