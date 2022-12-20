# 14696 딱지놀이 서브태스크 브론즈1
# https://www.acmicpc.net/problem/14696

import sys
sys.stdin = open('input.txt')


def solution():
    # 카운팅 리스트 만들기
    a_cnt = [0] * 5  # 0은 버리고, 1 ~ 4 담기
    b_cnt = [0] * 5
    for a_d in a_data:
        a_cnt[a_d] += 1
    for b_d in b_data:
        b_cnt[b_d] += 1
    # 크기 비교
    # 강함 : 별(4) > 동그라미(3) > 네모(2) > 세모(1)
    # 한 종류당 최대 100개 까지 가능, 생각보다 컴퓨터는 강함!
    points = [0, 1, 101, 101**2, 101**3]
    a_points = 0
    b_points = 0
    for i in range(1, 5):
        a_points += points[i] * a_cnt[i]
        b_points += points[i] * b_cnt[i]

    if a_points > b_points:
        return 'A'
    elif a_points < b_points:
        return 'B'
    else:
        return 'D'


N = int(input())  # 라운드 수  1 <= N <= 1000
for rnd in range(N):  # 라운드별
    a, *a_data = map(int, input().split())  # an : a의 개수, a = 그림정보
    b, *b_data = map(int, input().split())  # b의 경우
    print(solution())
