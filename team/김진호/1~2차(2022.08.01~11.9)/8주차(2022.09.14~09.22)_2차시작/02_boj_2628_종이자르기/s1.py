# https://www.acmicpc.net/problem/2628

import sys
sys.stdin = open("input.txt")

N,M = map(int,input().split())
rows = [0,N]
cols = [0,M]
for _ in range(int(input())):
    op, pos = map(int,input().split())
    if op == 0:
        cols.append(pos)
    else:
        rows.append(pos)
cols.sort()
rows.sort()
result = 0
for idx in range(len(rows)-1):
    for idx2 in range(len(cols)-1):
        width = (rows[idx+1] - rows[idx]) * (cols[idx2+1] - cols[idx2])
        if result < width:
            result = width
print(result)

print('<output>')
f = open("output.txt", 'r')
data = f.read()
print(data)
f.close()
