# 스택수열 - 실버2
# https://www.acmicpc.net/problem/1874

import sys
sys.stdin = open("input.txt")
# sys.stdin = open("input2.txt")


def solution():
    n = int(input())
    stack = []
    answer = []
    cur = 1

    for _ in range(n):
        target_num = int(input())

        while cur <= target_num:
            stack.append(cur)
            answer.append("+")
            cur += 1

        if stack[-1] == target_num:
            stack.pop()
            answer.append("-")
        else:
            print("NO")
            return

    for i in range(len(answer)):
        print(answer[i])

    return


solution()


# def solution():
#     n = int(input())
#     stack = [i for i in range(1, n+1)]
#     tmp = []
#     answer = []
#
#     for _ in range(n):
#         target_num = int(input())
#
#         if not stack:
#             print("NO")
#             return
#
#         while stack[-1] != target_num:
#             if stack[-1] > target_num:
#                 tmp.append(stack.pop())
#                 answer.append("+")
#             else:
#                 if tmp:
#                     stack.append(tmp.pop())
#                     answer.append("+")
#                 else:
#                     print("NO")
#                     return
#         stack.pop()
#         answer.append("-")
#
#     for i in range(len(answer)):
#         print(answer[i])
#
#     return
#
#
# solution()
