# 프로그래머스 lv2 마법의 엘레베이터
# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    num = str(storey)
    answer = 0
    tmp = 0
    for n in range(len(num) -1, -1, -1):
        n = int(n) + tmp
        if int(num[n]) <= 5:
            answer += int(num[n])
            tmp = 0
        else:
            answer += 10 - int(num[n])  # (다음 자리수에서 빼는 것이기 때문에)
            tmp = 1
    return answer


print(solution(16))  # 6
print("#" * 50)
print(solution(2554))  # 16
