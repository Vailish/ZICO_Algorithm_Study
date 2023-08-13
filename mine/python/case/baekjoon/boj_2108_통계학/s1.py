# 통계학 - 실버 3
# https://www.acmicpc.net/problem/2108


# 2초인데... 시간초과 -> pypy로 돌리니까 해결됨

import sys


sys.stdin = open("input3.txt")


def solution():
    lst = []
    my_lst = [0 for _ in range(8001)]
    for _ in range(int(input())):
        num = int(input())
        lst.append(num)
        my_lst[num+4000] += 1

    lst.sort()

    # 산술평균
    print(round(sum(lst)/len(lst)))

    # 중앙값
    print(lst[len(lst)//2])

    # 최빈값
    max_num = max(my_lst)
    if my_lst.count(max_num) > 1:
        cnt = 1

        for i in range(len(my_lst)):
            if my_lst[i] == 0:
                continue
            elif cnt == 2 and my_lst[i] == max_num:
                print(i-4000)
                break
            elif my_lst[i] == max_num:
                cnt += 1

    else:
        print(my_lst.index(max(my_lst))-4000)

    # 범위
    print(lst[-1] - lst[0])


solution()
