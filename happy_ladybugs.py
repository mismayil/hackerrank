'''
Problem: https://www.hackerrank.com/challenges/happy-ladybugs
'''

Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()

    alpha = [0] * 27
    happy = True

    if len(b) <= 1:
        if b[0] == '_': print('YES')
        else: print('NO')
    else:
        for i in b:
            if i == '_': alpha[0] += 1
            else: alpha[ord(i)-64] += 1

        if alpha[0] == 0:
            for i in range(0, n):
                if (i-1 < 0 or b[i] != b[i-1]) and (i+1 > n-1 or b[i] != b[i+1]): happy = False
            if happy: print('YES')
            else: print('NO')
        else:
            if alpha[1:].count(1) > 0: print('NO')
            else: print('YES')
