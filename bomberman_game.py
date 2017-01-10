import sys

NOTHING = -2
EMPTY = -1
BOMB = 0
EXPIRED = 3

r, c, n = [int(i) for i in input().strip().split(' ')]
grid = []
confs = {}

for i in range(r):
    line = input().strip()
    row = []
    for j in range(c):
        if line[j] == '.': row.append(NOTHING)
        else: row.append(BOMB)           
    grid.append(row)
    
# next second
def evolve():
    for i in range(r):
        for j in range(c):
            grid[i][j] += 1
            
# detonate
def detonate():
    for i in range(r):
        for j in range(c):
            if grid[i][j] == EXPIRED:
                grid[i][j] = EMPTY
                if i-1 >= 0 and grid[i-1][j] != EXPIRED: grid[i-1][j] = EMPTY
                if i+1 < r and grid[i+1][j] != EXPIRED: grid[i+1][j] = EMPTY    
                if j-1 >= 0 and grid[i][j-1] != EXPIRED: grid[i][j-1] = EMPTY
                if j+1 < c and grid[i][j+1] != EXPIRED: grid[i][j+1] = EMPTY

# check conf if repeated
def check():
    for i in range(r):
        for j in range(c):
            if grid[i][j] != confs[0][i][j]: return False
    return True

# save conf
def save(index):
    confs[index] = []
    for i in range(r):
        confs[index].append(grid[i][:])

# print grid
def output(conf):
    for i in range(r):
        for j in range(c):
            if conf[i][j] < 0: print('.', end='')
            else: print('O', end='')
        print()
        
# 3 secs passed
for s in range(EXPIRED): 
    if n == s: 
        output(grid)
        sys.exit()
    evolve()

detonate()

index = 0    
repeated = False

while (not repeated):
    save(index)
    evolve()
    detonate()
    repeated = check()
    index += 1
    
index = (n - EXPIRED) % len(list(confs.keys()))
output(confs[index])