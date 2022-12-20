# 67256. 키패드 누르기
# https://school.programmers.co.kr/learn/courses/30/lessons/67256


# def solution(numbers, hand):
#     result = ''
#     l_now, r_now = 0, 0
#     for num in numbers:
#         if num % 3 == 1:
#             l_now = num
#             result += 'L'
#         elif num % 3 == 0:
#             r_now = num
#             result += 'R'
#         else:
#             l, r = abs(l_now - num), abs(r_now - num)
#             print('-', l, r)
#             if l < r:
#                 l_now = num
#                 result += 'L'
#             elif l > r:
#                 r_now = num
#                 result += 'R'
# else:
#     f = hand[0].upper()
#     result += f
#     if f == 'R':
#         r_now = num
#     else:
#         l_now = num

#         print(l_now, r_now, num)
#     return result


# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))ㄴ


def solution(numbers, hand):
    result = ''
    lx, ly = 2, 3
    rx, ry = 0, 3
    for num in numbers:
        if num == 0:
            num = 11
        x = ((num % 3) * 2) % 3
        y = num // 3 if x else num // 3 - 1
        l = abs(lx - x) + abs(ly - y)
        r = abs(rx - x) + abs(ry - y)
        if num % 3 == 1:
            lx, ly = x, y
            result += 'L'
        elif num % 3 == 0:
            rx, ry = x, y
            result += 'R'
        else:
            if l > r:
                rx, ry = x, y
                result += 'R'
            elif l < r:
                lx, ly = x, y
                result += 'L'
            else:
                if hand == 'right':
                    rx, ry = x, y
                    result += 'R'
                else:
                    lx, ly = x, y
                    result += 'L'
    return result


# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
