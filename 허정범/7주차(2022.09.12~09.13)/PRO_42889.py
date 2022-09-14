def solution(N, stages):
    answer = []
    stage_probability = []
    # 스테이지 마다 실패율 구하기
    for i in range(1, N + 1):
        count = 0  # 도전한사람중 실패한사람
        user = 0  # 도전자
        for stage in stages:
            if i <= stage:
                user += 1
                if i == stage:
                    count += 1

        if user == 0:
            probability = 0
        else:
            probability = count / user
        stage_probability.append((probability, i))

    # # 정렬 시키기
    # for j in range(N - 1, 0, -1):
    #     for k in range(0, j):
    #         if stage_probability[k][0] < stage_probability[k + 1][0]:
    #             stage_probability[k], stage_probability[k + 1] = (
    #                 stage_probability[k + 1],
    #                 stage_probability[k],
    #             )

    for m in sorted(stage_probability, key=lambda x: -x[0]):
        answer.append(m[1])
    return answer


print(solution(4, [4, 4, 4, 4, 4]))
