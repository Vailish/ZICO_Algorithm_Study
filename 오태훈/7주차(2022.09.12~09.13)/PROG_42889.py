# 42889. 실패율
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

# 실패율
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수


def solution(N, stages):
    # 스테이지 별 플레이어 수를 세기 위한 딕셔너리
    dict_cnt = {}
    # 총 플레이어 수
    players = len(stages)
    # 스테이지 별 실패율을 저장하기 위한 딕셔너리
    result = {}
    # 스테이지 별 플레이어 수 계산
    for stage in stages:
        if stage in dict_cnt:
            dict_cnt[stage] += 1
        else:
            dict_cnt[stage] = 1
    # 지금까지 실패한 플레이어를 저장할 변수 cnt
    cnt = 0
    # 실패율 계산
    for stage_num in range(1, N + 1):
        if stage_num in dict_cnt:
            fail_player = dict_cnt[stage_num]
            pass_player = players - cnt
            cnt += fail_player
            result[stage_num] = fail_player / pass_player
        else:
            result[stage_num] = 0
    # result = [m[0] for m in sorted(result.items(), key=lambda x: x[1], reverse=True)]
    # value를 기준으로 내림차순 정렬
    return sorted(result, key=lambda x: result[x], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
