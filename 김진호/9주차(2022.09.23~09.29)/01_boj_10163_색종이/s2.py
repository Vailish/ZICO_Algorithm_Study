import sys
sys.stdin = open("input.txt")

N = int(input())
maps = [[-1]*1001 for _ in range(1001)]
command = [list(map(int,input().split())) for _ in range(N)]
result = [0]*N
for k in range(N-1,-1,-1):
    x, y, width, height = command[k]
    for i in range(x,x+width):
        for j in range(y,y+height):
            if maps[i][j] == -1:
                maps[i][j] = k
                result[k] += 1

for r in result:
    print(r)


print('<output>')
f = open("output.txt", 'r')
data = f.read()
print(data)
f.close()
