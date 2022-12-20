# 실패율
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    # stages : 유저의 현 스테이지
    # N : 전체 스테이지 개수
    # 실패율 : 스테이지 도달 & 클리어X / 스테이지 도달

    # 누적 카운트 함수 -> 누적 클리어한 수
    cnt = [0] * (N)
    cnts = [1] + [0] * (N-1)

    for stage in stages:
        cnt[stage-1] += 1

    for i in range(1, N):
        cnts[i] += cnts[i - 1]

    fail_rate = [[]]
    for i in range(N):
        if cnts[i] == 0:
            fail_rate.append([i, 0])
        else:
            fail_rate.append([i, cnt[i] / cnts[i]])

    answer = []
    for stage, value in sorted(fail_rate):
        answer.append(stage)

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
