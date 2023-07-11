# 직사각형 별찍기 12969
# https://school.programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().split())
[print('*' * a) for _ in range(b)]


# a, b = map(int, input().strip().split(' '))
# answer = ('*'*a +'\n')*b
# print(answer)
