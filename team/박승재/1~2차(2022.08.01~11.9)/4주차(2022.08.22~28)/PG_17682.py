# import re
#
# string = input()
# numbers = re.findall(r'\d+', string)
# bonus = re.findall('[a-zA-Z][#*]?', string)
# print(numbers, bonus)
# result = 0
# for n in range(2, -1, -1):
#     number = int(numbers[n])
#     for p in bonus[n]:
#         if p == 'D':
#             number = number ** 2
#         elif p == 'T':
#             number = number ** 3
#         elif p == '#':
#             number = number * (-1)
#
#     result += number
# print(result)


# def solution(dartResult):
#     string = dartResult
#     word = ''
#     signal = True
#     for i in range(len(string)):
#         if signal:
#             if string[i].isdigit():
#                 word += ' ' + string[i]
#                 if string[i + 1].isdigit():
#                     word += string[i + 1]
#                     # string.replace(string[i + 1], ' ')
#                     signal = False
#             else:
#                 word += string[i]
#         else:
#             signal = True
#
#     word_list = list(word.split())
#     result = []
#     signal = []
#     for n in range(3):
#         num = ''
#         for i in word_list[n]:
#             if i.isdigit():
#                 num += i
#             elif i == 'S':
#                 nu = int(num)
#             elif i == 'D':
#                 nu = int(num) ** 2
#             elif i == 'T':
#                 nu = int(num) ** 3
#             elif i == '#':
#                 nu = nu * (-1)
#             elif i == '*':
#                 signal.append(n)
#         result.append(nu)
#     if signal:
#         for i in signal:
#             if i == 0:
#                 result[i] = result[i] * 2
#             else:
#                 result[i - 1] = result[i - 1] * 2
#                 result[i] = result[i] * 2
#     return sum(result)
#
# print(solution(input()))


# def solution(dartResult):
#     answer = [0, 1]
#     dartResult = dartResult.replace('10','k')
#     point = ['10' if i == 'k' else i for i in dartResult]
#     bonus = (0, 'S', 'D', 'T')
#     sig = 0
#
#     for i in point:
#         if i.isdigit():
#             answer.append(int(i))
#             sig += 1
#         elif i in bonus:
#             answer[sig] = answer[sig] ** bonus.index(i)
#         elif i == '#':
#             answer[sig] = answer[sig] * (-1)
#         else:
#             if sig == 1:
#                 answer[sig] = answer[sig] * 2
#             else:
#                 answer[sig-1] = answer[sig-1] * 2
#                 answer[sig] = answer[sig] * 2
#     return sum(answer)
#
#
# print(solution(input()))