'''
Problem: https://www.hackerrank.com/challenges/absolute-permutation
'''

def checkperm(perm, k):
    for i in range(n):
        neg = (i+1) - k
        pos = (i+1) + k

        try:
            if neg <= 0: raise ValueError
            negi = i + perm[i:].index(neg)
            perm[i], perm[negi] = perm[negi], perm[i]
        except ValueError:
            try:
                if pos > n: raise ValueError
                posi = i + perm[i:].index(pos)
                perm[i], perm[posi] = perm[posi], perm[i]
            except ValueError:
                return [-1]

    return perm

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    perm = []

    for i in range(n):
        perm.append(i+1)

    perm = checkperm(perm, k)
    print(' '.join(str(x) for x in perm))
