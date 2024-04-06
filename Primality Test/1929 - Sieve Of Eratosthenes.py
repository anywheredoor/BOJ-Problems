"""
https://www.acmicpc.net/problem/1929 (소수 구하기)

Mathematics
Number Theory
Primality Test
Sieve Of Eratosthenes

Solved with Sieve Of Eratosthenes
"""

import sys
import math

M, N = map(int, sys.stdin.readline().split())

is_prime = [True]*(N+1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime[i]:
        j = 2
        while i * j <= N:
            is_prime[i * j] = False
            j += 1

for i in range(M, N+1):
    if is_prime[i]:
        print(i)
