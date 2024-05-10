"""
https://www.acmicpc.net/problem/2083 (럭비 클럽)

Implementation
"""

import sys

while True:
    name, age, weight = sys.stdin.readline().split()

    if name + age + weight == "#00":
        sys.exit()
    elif int(age) > 17 or int(weight) >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")
