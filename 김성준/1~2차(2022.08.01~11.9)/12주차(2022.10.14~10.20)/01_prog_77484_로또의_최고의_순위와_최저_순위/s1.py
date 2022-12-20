# 로또의 최고 순위와 최저 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484

wins = [6, 6, 5, 4, 3, 2, 1]


def solution(lottos, win_nums):
    cnt = 0
    zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
        if lotto == 0:
            zero += 1
    answer = sorted([wins[cnt], wins[cnt+zero]])
    return answer
