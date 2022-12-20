import sys
sys.stdin = open("input.txt")

N = int(input())
maps = [[-1]*1001 for _ in range(1001)]
result = [0]*N
for k in range(N):
    x, y, width, height = map(int,input().split())
    for i in range(x,x+width):
        for j in range(y,y+height):
            maps[i][j] = k

for i in range(1001):
    for j in range(1001):
        if maps[i][j] != -1:
            result[maps[i][j]] += 1

for r in result:
    print(r)


print('<output>')
f = open("output.txt", 'r')
data = f.read()
print(data)
f.close()
