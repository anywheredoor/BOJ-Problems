"""
https://www.acmicpc.net/problem/23795 (사장님 도박은 재미로 하셔야 합니다)

Mathematics
Implementation
Arithmetic
"""
import sys

total = 0

while True:
    n = int(sys.stdin.readline())
    
    if n == -1:
        print(total)
        sys.exit()
        
    total += n
