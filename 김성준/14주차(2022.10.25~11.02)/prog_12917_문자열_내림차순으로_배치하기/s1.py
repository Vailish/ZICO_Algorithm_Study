# prog_12917 문자열 내림차순으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12917

# 65 ~ 90 = A ~ Z
# 97 ~ 122 = a ~ z

def solution(s):
    # 65 ~ 90 = A ~ Z
    # 97 ~ 122 = a ~ z
    chrs_lower = []
    chrs_upper = []
    for chr in s:
        if ord(chr) > 90:
            chrs_lower.append(chr)
        else:
            chrs_upper.append(chr)
    answer = sorted(chrs_lower)[::-1] + sorted(chrs_upper)[::-1]
    return ''.join(answer)

# 문제 조건상 굳이 따로 분리해서 할 필요 없음...
# def solution(s):
#     return ''.join(sorted(s, reverse=True))
# 이러면 끝;