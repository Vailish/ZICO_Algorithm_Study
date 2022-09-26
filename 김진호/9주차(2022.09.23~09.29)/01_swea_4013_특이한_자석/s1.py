import sys
sys.stdin = open("input.txt")

def f(num,rotation,pos):
    if 0 <= num < 4 and maps[num][2 * -1 * pos] != maps[num-pos][2 * pos]:
        f(num+pos, rotation * -1, pos)



for test_case in range(1,int(input())+1):
    actions = int(input())
    maps = [list(map(int,input().split())) for _ in range(4)]
    for _ in range(actions):
        num, rotation = map(int,input().split())
        num -= 1
        f(num-1, rotation, -1)
        f(num+1, rotation, 1)

    print(max(result,increase_length,decrease_length))


print('<output>')
f = open("output.txt", 'r')
data = f.read()
print(data)
f.close()