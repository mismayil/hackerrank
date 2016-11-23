import sys
import math

t = int(input().strip())

n = t // 3
if n > 1: n = math.floor(math.log(n, 2))
    
if n ==0: p = 0
else: p = 3

for i in range(n-1):
    p += 3 * (2 ** (i+1))
    
print(3 * (2 ** n) - (t - (p + 1)))