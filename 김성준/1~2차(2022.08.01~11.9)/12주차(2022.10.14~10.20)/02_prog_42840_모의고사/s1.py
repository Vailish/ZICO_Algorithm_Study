# programmers 42840 모의고사
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    result = []
    one = [1, 2, 3, 4, 5]  # 5개
    two = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10개

    score = [0, 0, 0]  # 순서대로

    for n in range(len(answers)):
        # 1번 수포자가 맞춘 개수
        if one[n % 5] == answers[n]:
            score[0] += 1
        # 2번 수포자가 맞춘 개수
        if two[n % 8] == answers[n]:
            score[1] += 1
        # 3번 수포자가 맞춘 개수
        if three[n % 10] == answers[n]:
            score[2] += 1

    # 최대값 구하기
    max_num = max(score)
    result = []
    # 동점자 구하기
    for i in range(3):
        if score[i] == max_num:
            result.append(i + 1)
    return result
