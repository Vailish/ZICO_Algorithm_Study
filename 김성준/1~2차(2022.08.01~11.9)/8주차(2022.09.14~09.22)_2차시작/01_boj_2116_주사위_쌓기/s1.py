# 주사위 쌓기 골드4
# https://www.acmicpc.net/problem/2116


import sys
sys.stdin = open('input.txt')


def max_num(top, bottom):
    lst = [1, 2, 3, 4, 5, 6]
    lst.remove(top)
    lst.remove(bottom)
    return max(lst)


def solution(dices):
    dice_numbers = len(dices)
    opposite_sides = []
    result = []
    # 마주보는 면 담은 튜플 생성
    # opposite_sites = [[(0, 5), (1, 3), (2, 4)], [2번주사위], ...]
    for num in range(dice_numbers):
        opposite_sides.append([
            (dices[num][0], dices[num][5]),   # A, F
            (dices[num][1], dices[num][3]),   # B, D
            (dices[num][2], dices[num][4])])  # C, E
    # 주사위 연결하기
    for i in range(3):
        for n in range(2):
            stack = []  # stack 초기화
            temp = 0
            stack.append((opposite_sides[0][i][n-1], opposite_sides[0][i][n]))  # 뒤가 연결 부분

            # 첫 번째 주사위를 제외하고 붙여주기
            for dice in range(1, dice_numbers):
                bottom, top = stack.pop()

                # 위 아래 제거후 더해주기
                temp += max_num(top, bottom)

                # 주사위 연결하기
                for j in range(3):
                    if top in opposite_sides[dice][j]:
                        t = opposite_sides[dice][j].index(top)
                        stack.append((opposite_sides[dice][j][t], (opposite_sides[dice][j][t-1])))
                        break

                # for j in range(3):
                #     if top == opposite_sides[dice][j][0]:
                #         stack.append((opposite_sides[dice][j][0], opposite_sides[dice][j][1]))
                #         break
                #     if top == opposite_sides[dice][j][1]:
                #         stack.append((opposite_sides[dice][j][1], opposite_sides[dice][j][0]))
                #         break

            # 마지막 주사위 더해주기
            bottom, top = stack.pop()
            temp += max_num(top, bottom)
            result.append(temp)
    return max(result)


dices = []
for _ in range(int(input())):
     dices.append(list(map(int, input().split())))  # dices = [[2,3,1,6,5,4], [주사위2], ...]
print(solution(dices))
