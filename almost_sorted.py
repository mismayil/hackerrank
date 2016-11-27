def asorted(d, n):
    i = 0
    sorte = True

    for i in range(n-1):
        if d[i] > d[i+1]:
            sorte = False
            break

    if sorte: return 'yes'

    j = i+1
    for j in range(i+1, n-1):
        if d[j] < d[j+1]: break

    op = ''
    if j-i == 1:
        op = 'swap'
        for k in range(j+1, n):
            if d[k] < d[j]: j = k
        d[i], d[j] = d[j], d[i]
    else:
        op = 'reverse'
        t = d[i:j+1]
        t.reverse()
        d[i:j+1] = t

    for k in range(n-1):
        if d[k] > d[k+1]: return 'no'

    return 'yes\n' + op + ' ' + str(i+1) + ' ' + str(j+1)

n = int(input().strip())
d = [int(i) for i in input().strip().split(' ')]

print(asorted(d, n))
