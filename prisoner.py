'''
Problem: https://www.hackerrank.com/challenges/save-the-prisoner
'''

t = int(input().strip())

for i in range(t):
    n,m,s = input().strip().split()
    n,m,s = [int(n), int(m), int(s)]
    k = m - (1 + (n - s))
    if k % n == 0: print(n)
    else: print(k % n)
