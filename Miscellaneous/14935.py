"""
https://www.acmicpc.net/problem/14935 (FA)

Mathematics
Implementation
Ad-hoc
"""
import sys

x = input()

previous = x

while True:
    x = str(int(x[0]) * len(x))

    if x == previous:
        print("FA")
        sys.exit()

    previous = x

print("NFA")
