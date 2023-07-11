# 2116. 주사위 쌓기
# https://www.acmicpc.net/problem/2116

import sys
import copy

input = sys.stdin.readline

n = int(input())

dices = [list(map(int, input().split())) for i in range(n)]
dice_index = [5, 3, 4, 1, 2, 0]
result_arr = []
for top in range(1, 7):
    sum_num = 0
    for j in range(n):
        now_dice = copy.deepcopy(dices[j])
        bottom = top
        bottom_idx = dices[j].index(top)
        top_idx = dice_index[bottom_idx]
        top = now_dice.pop(top_idx)

        now_dice.pop(now_dice.index(bottom))

        sum_num += max(now_dice)

    result_arr.append(sum_num)
print(max(result_arr))
