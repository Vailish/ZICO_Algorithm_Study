# prog_12903_가운데_글자_가져오기
# https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    length = len(s)
    if length % 2:
        answer = s[length // 2]
    else:
        answer = s[length // 2 - 1:length // 2 + 1]

    return answer