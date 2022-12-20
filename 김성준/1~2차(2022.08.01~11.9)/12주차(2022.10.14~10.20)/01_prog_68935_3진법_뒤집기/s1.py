# 3진법 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)

    return int(rev_base, 3)