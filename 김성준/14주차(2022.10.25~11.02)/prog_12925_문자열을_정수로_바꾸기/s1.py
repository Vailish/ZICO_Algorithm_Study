# prog_12925 문자열을 정수로 바꾸기
# https://school.programmers.co.kr/learn/courses/30/lessons/12925

def solution(s):
    answer = ''
    if s[0] == '+':
        answer = int(s[1:])
    elif s[0] == '-':
        answer = int(s[1:]) * (-1)
    else:
        answer = int(s)
    return answer
