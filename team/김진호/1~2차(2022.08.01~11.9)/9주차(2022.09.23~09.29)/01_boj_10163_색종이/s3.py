import sys
sys.stdin = open("input.txt")

N = int(input())
maps = [[-1]*1001 for _ in range(1001)]
command = [list(map(int,input().split())) for _ in range(N)]
result = [0]*N
for k in range(N):
    x, y, width, height = command[k]
    for w in range(width):
        maps[x+w][y:y+height] = [k]*height

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
