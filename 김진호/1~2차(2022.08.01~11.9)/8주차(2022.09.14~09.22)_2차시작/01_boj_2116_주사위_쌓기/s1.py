# https://www.acmicpc.net/problem/2116

import sys
sys.stdin = open("input.txt")


def chk_sum():
    print(num_list)


def make_list(top_idx,top,dice_num):
    if dice_num == N-1:
        chk_sum()
    temp = []
    for idx in range(6):
        if idx != top_idx or idx != top_idx+1:
            temp.append(dices[dice_num][idx])
    num_list.append(temp)
    make_list(dices[dice_num+1].index(top), dice_num + 1)
    num_list.pop()


N = int(input())
dices = []
result = 0
for _ in range(N):
    A,B,C,D,E,F = map(int,input().split())
    # dices.append((A,C,B,F,E,D))             # 기존 다이스 배열에서 0-3,1-4,2-5 를 짝짓도록 구조 변경
    dices.append((A, F, C, E, B, D))        # 기존 다이스 배열에서 0-1,2-3,4-5 를 짝짓도록 구조 변경
for n in range(6):
    num_list = []
    make_list(n,dices[0][n],0)


# print('<output>')
# f = open("output.txt", 'r')
# data = f.read()
# print(data)
# f.close()
