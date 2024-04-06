"""
https://www.acmicpc.net/problem/1978 (소수 찾기)

Mathematics
Number Theory
Primality Test
"""

import sys
import math

def is_prime_number(x):
    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
            
    return True

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
cnt = 0

for x in array:
    if is_prime_number(x):
        cnt += 1

print(cnt)
