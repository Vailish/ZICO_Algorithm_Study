# from itertools import combinations
#
#
# def check(a, b):
#     if a == b:
#         return True
#     elif a > b:
#         for n, m in [(2, 3), (2, 4), (3, 4)]:
#             if a * n == b * m:
#                 return True
#     else:
#         for n, m in [(2, 3), (2, 4), (3, 4)]:
#             # print((b, a), (n * a, m * b))
#             if b * n == a * m:
#                 return True
#     return False
#
#
# # def solution(weights):
# #     answer = 0
# #
# #     # 완전탐색
# #     # 콤비네이션으로 빼준다
# #     for a, b in combinations(weights, 2):
# #         if check(a, b):
# #             answer += 1
# #     return answer
#
# def solution(weights):
#     answer = 0
#     # 정렬
#     weights.sort()
#
#     # idx로 비교해서 check
#     for idx in range(len(weights) - 1):
#         print((weights[idx], weights[idx + 1]), check(weights[idx], weights[idx + 1]))
#         if check(weights[idx], weights[idx + 1]):
#             answer += 1
#
#     return answer
#

from collections import Counter


def solution(weights):
    answer = 0

    # 1:1 처리
    for k, v in Counter(weights).items():
        if v > 1:
            answer += v * (v - 1) // 2

    # 1 : 1/2 3/4 3/2 처리
    for weight in set(weights):
        for rate in [1 / 2, 3 / 4, 3 / 2]:
            if weight * rate in weights:
                answer += weights.count(weight) * weights.count(weight * rate)
    print(answer)
    return answer

print(solution([100,180,360,100,270]))
