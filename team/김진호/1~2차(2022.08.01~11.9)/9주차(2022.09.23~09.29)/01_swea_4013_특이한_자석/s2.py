import sys
from collections import deque
sys.stdin = open("input.txt")

###########################
# 현재 돌려야하는 톱니의 좌우에 맞닿은 톱날을 확인하고
# 같이 돌아가는지, 아닌지를 판단할수있어야한다
# 만약 돌리기 시작한 위치부터 톱니를 돌려버린다면 다른 톱니에서 확인이 어려울것같아서
# dfs 형식을 사용하여 일단 돌려야할 제일 마지막 톱니까지 가도록한뒤 그 톱니부터 돌리면서
# 빠져나오도록 작성하였다
# 이번 문제는 톱니가 4개 일직선이여서 상관이 없지만 이후에 더 많은 톱니가 여러방향으로 존재한다면
# 이런식으로 작성된 코딩이 처리하기에 더 쉬울것같다
###########################


def f(num,rot,pos):            # 어느 위치에서 호출되어도 작동하는 f 함수 작성
    if 0 <= num < 4 and maps[num][2 * -pos] != maps[num-pos][2 * pos]:
        # num == 바퀴 번호인데 -1 되어있으므로 0~3일때만 확인.
        # 아래에서 호출될때 num-1, num+1 로 호출하였기때문에 현재 num은 왼쪽 혹은 오른쪽의 바퀴이며
        # pos를 통해서 -1이면 왼쪽톱니 1이면 오른쪽 톱니이다.
        # if문으로 이 pos에 따라 나눌수있지만, [6]과 [-2]가 같은 위치라는 점을 이용해서 한줄로 판별해본다.
        # 왼쪽 톱니일경우 현재 톱니에서 [2]를 옆에있는 톱니에서 [6]이 같은지 비교해야한다.
        # [2 * -1 * pos] = 2 , [2 * pos] = -2 = 6 으로 이 식을 만족한다.
        # 마찬가지로 오른쪽 톱니일경우에 [-2] [2] 식으로 이 식을 만족한다.
        f(num+pos, -rot, pos)  # 다음 톱니를 확인하는 f 함수 재호출
        maps[num].rotate(rot)  # 현재 톱니 rotate
        # if rotation == 1:
        #     temp = maps[num].pop()
        #     maps[num].appendleft(temp)
        # else:
        #     temp = maps[num].popleft()
        #     maps[num].append(temp)


for test_case in range(1,int(input())+1):
    act = int(input())
    maps = [deque(map(int,input().split())) for _ in range(4)]
    for _ in range(act):
        num, rot = map(int,input().split())
        num -= 1                # 배열 인덱스값 맞추기
        f(num-1, -rot, -1)      # 왼쪽 톱니 확인하는 f 함수 호출
        f(num+1, -rot, 1)       # 오른쪽 톱니 확인하는 f 함수 호출
        maps[num].rotate(rot)   # 현재 톱니 rotate
        # if rotation == 1:
        #     temp = maps[num].pop()
        #     maps[num].appendleft(temp)
        # else:
        #     temp = maps[num].popleft()
        #     maps[num].append(temp)
    result = maps[0][0]+maps[1][0]*2+maps[2][0]*4+maps[3][0]*8
    print(f'#{test_case} {result}')


print('<output>')
f = open("output.txt", 'r')
data = f.read()
print(data)
f.close()