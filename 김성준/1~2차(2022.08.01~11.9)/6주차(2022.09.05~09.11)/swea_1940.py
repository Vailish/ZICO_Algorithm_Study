# 1940. 가랏! RC카! D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjMgaALgDFAUq

def solution(data):
    commands = data
    speed = 0  # 현재 속도
    distance = 0  # 총 이동 거리
    for command, spd in commands:
        # 0의 경우에는 그냥 속도 그대로 더해주면 됨
        if command == 1:
            speed += spd
        elif command == 2:
            speed -= spd
            if speed < 0:
                speed = 0
        distance += speed
    return distance


for case in range(1, 1 + int(input())):
    queue = []
    for _ in range(int(input())):
        value = list(map(int, input().split()))
        if value == [0]:  # 인덱스 오류 제거용
            queue.append([0, 0])
        else:
            queue.append(value)
    print(f'#{case} {solution(queue)}')


# 1 2 -> 가속 감속속


# def soution(datas):
#     commands = datas
#     spd = 0
#     distance = 0
#     for command in commands:
#         if command == 2:
#             spd += 1
#         else:
#             spd -= 1
#             if spd <= 0:
#                 spd == 0
#             else:
#                 distance += spd
#     result += distance
#
#
# global result
# for case in range(1, 1 + int(input())):
#     result = 0
#     for _ in range(int(input())):
#         data = map(int, input().split())
#         if data != 0:
#            solution(data)
#     print(f'{case} {result}')
#
