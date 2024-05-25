"""
https://www.acmicpc.net/problem/15873 (공백 없는 A+B)

Mathematics
Arithmetic
Case Work
"""
data = input()

if len(data) == 3:
    if data[:2] == "10":
        print(int(data[:2]) + int(data[2]))
    else:
        print(int(data[0]) + int(data[1:3]))
elif len(data) == 4:
    print(20)
else:
    print(int(data[0]) + int(data[1]))
