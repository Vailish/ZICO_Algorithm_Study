# prog_12912 문자열 내 p와 y의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    s = s.lower()
    p = s.count('p')
    y = s.count('y')
    print(s)
    print(p, y)
    if p == 0 and y == 0:
        return True
    return True if p == y else False

# 이게 뭐지?
# def solution():
#     n = int(input())
#     texts = [[] for _ in range(51)]
#     for _ in range(n):
#         chr = input()
#         texts[len(chr)].append(chr)
#     answer = []
#     for chrs in texts[1:]:
#         chrs.sort()
#     for chrs in texts:
#         if chrs:
#             for ch in chrs:
#                 if ch not in answer:
#                     answer.append(ch)
#     return answer
#
# print('\n'.join(solution()))
