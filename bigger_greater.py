t = int(input().strip())
ws = [input().strip() for i in range(t)]

for w in ws:
    lex = False
    k = None
    for i in range(len(w)-1, -1, -1):
        for j in range(i+1, len(w)):
            if w[i] < w[j]:
                lex = True
                if k == None or w[j] < w[k]: k = j
        if lex: break
    if lex:
        w = w[:i] + w[k] + ''.join(sorted(w[i+1:k] + w[i] + w[k+1:])) 
        print(w)
    else: print('no answer')