n, k = input().strip().split(' ')
n, k = [int(n), int(k)]

a = [int(i) for i in input().strip().split(' ')]

mods = [i % k for i in a]
temp = [0] * k
ans = 0

for i in range(n):
    temp[mods[i]] += 1
    
m = max(temp)

while m != 0:
    index = temp.index(m)
    if index == 0 or index * 2 == k: ans += 1
    else: ans += m
    temp[index] = 0
    temp[(k-index)%k] = 0
    m = max(temp)

print(ans)