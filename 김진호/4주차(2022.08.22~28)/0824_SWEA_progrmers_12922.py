# 수박수박수박수박수박..
# https://school.programmers.co.kr/learn/courses/30/lessons/12922?language=python3

def solution(n):
    return "수박" * (n // 2) + "수" * (n % 2)


print(solution(10))
# 수박수박수박수박수박
print(solution(11))
# 수박수박수박수박수박수