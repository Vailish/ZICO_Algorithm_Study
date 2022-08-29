# [1차] 다트 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

# def solution(dartResult):
#     stack = []
#     for idx in dartResult:
#         if idx != idx[-1] and idx
#             if idx in '0123456789':
#                 stack.append(int(idx))
#         elif idx in 'SDT':
#             if idx == 'S':
#                 pass
#             elif idx == 'D':
#                 stack.append(stack.pop() ** 2)
#             else: # idx == 'T'
#                 stack.append(stack.pop() ** 3)
#         elif idx in '*#':
#             if idx == '*':
#                 temp = stack.pop() * 2
#                 if len(stack) >= 1:
#                     stack.append(stack.pop() * 2)
#                 stack.append(temp)
#             else: # '#'
#                 stack.append(stack.pop() * (-1))
#     return sum(stack)

# import re

def solution(dartResult):
    stack = []
    signal = True
    for num in range(len(dartResult)):  # while 문으로 +1 더 해서 넘기기
        if not signal:
            signal = True
        elif dartResult[num] == '1' and dartResult[num+1] == '0':
            stack.append(10)
            signal = False
        else:
            if dartResult[num] in '0123456789':
                stack.append(int(dartResult[num]))
            elif dartResult[num] in 'SDT':
                if dartResult[num] == 'S':
                    pass
                elif dartResult[num] == 'D':
                    stack.append(stack.pop() ** 2)
                else: # dartResult[num] == 'T'
                    stack.append(stack.pop() ** 3)
            elif dartResult[num] in '#*':
                if dartResult[num] == '*':
                    temp = stack.pop() * 2
                    if len(stack) >= 1:
                        stack.append(stack.pop() * 2)
                    stack.append(temp)
                else: # '#'
                    stack.append(stack.pop() * (-1))
    return sum(stack)

print(solution('1D2S#10S'))
