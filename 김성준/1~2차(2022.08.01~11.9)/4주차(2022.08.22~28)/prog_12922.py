# 12922. 수박수박수박수박수박수?
# https://school.programmers.co.kr/learn/courses/30/lessons/12922

# def solution(n):
#     answer = ''
#
#     for num in range(n):
#         if num % 2:
#             answer += '박'
#         else:
#             answer += '수'
#
#     return answer

# def water_melon(n):
#     s = "수박" * n
#     return s[:n]

# def water_melon(n):
#     return "수박"*(n//2) + "수"*(n%2)

# def water_melon(n):
#     return ("수박"*n)[0:n]

import itertools

수박 = itertools.cycle("수박")

for ch in range(int(input())):
    print(수박.next(), end='')
