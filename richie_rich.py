'''
Problem: https://www.hackerrank.com/challenges/richie-rich
'''

import sys

def makepal(n, k, number):
    
    i = 0
    m = 0
    
    if n % 2 == 0: m = n // 2
    else: m = n // 2 + 1
        
    for i in range(m):
        if number[i] == number[n-i-1]: continue
        if k > 0: k -= 1
        else: return -1
    
    for i in range(m):
        if number[i] == number[n-i-1]:
            if number[i] != '9':
                if i == n-i-1:
                    if k > 0: 
                        number[i] = '9'
                        k -= 1
                else:
                    if k > 1:
                        number[i], number[n-i-1] = '9', '9'
                        k -= 2
        else:
            if number[i] > number[n-i-1]: number[n-i-1] = number[i]
            else: number[i] = number[n-i-1]   
            if number[i] != '9':
                if k > 0:
                    number[i], number[n-i-1] = '9', '9'
                    k -= 1               
     
    return ''.join(number)

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
number = input().strip()
number = list(number)

print(makepal(n, k, number))
