"""
https://www.acmicpc.net/problem/15059 (Hard choice)

Mathematics
Implementation
Arithmetic
"""
Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())

C = Cr - Ca
B = Br - Ba
P = Pr - Pa

my_list = (C, B, P)

total = 0

for food in my_list:
    if food > 0:
        total += food

print(total)
