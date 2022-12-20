# 1940. 가랏! RC카!
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjMgaALgDFAUq

for t in range(1, int(input()) + 1):
    n = int(input())
    cmds = [list(map(int, input().split())) for _ in range(n)]

    speed, distance = 0, 0
    for cmd in cmds:
        if cmd[0] == 1:
            speed += cmd[1]
        elif cmd[0] == 2:
            speed -= cmd[1]
            if speed < 0:
                speed = 0
        distance += speed
    print(f'#{t} {distance}')
