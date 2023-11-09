# 패션왕 신해빈 - silver3
# https://www.acmicpc.net/problem/9375

def solution():
    n = int(input())

    for _ in range(n):
        num = int(input())
        my_dict = dict()
        lst = []
        for i in range(num):
            # 종류의 길이 * 종류의 길이 .... - 1(한가지가 아니라면)
            goods, kind =input().split()
            if kind not in my_dict:
                my_dict[kind] = [goods]
                lst.append(kind)
            else:
                my_dict[kind].append(goods)

        if len(my_dict) == 1:
            print(len(my_dict[lst[0]]))
        else:
            tmp = 1
            for key in my_dict.keys():
                tmp *= len(my_dict[key]) + 1
            print(tmp - 1)


solution()
