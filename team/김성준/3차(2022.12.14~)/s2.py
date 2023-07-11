    # 받을 수 있냐 없냐
    ### 못받는 조건 : 두 점수 모두 제일 낮은 수일 때
    ### 받는다면 몇 등이냐(합)
def solution(scores):
    rank = 1

    ho_sum_score = scores[0] # 완호의 점수

    for idx in range(1, len(scores)):
        if scores[idx][0] > scores[0][0] and scores[idx][1] > scores[0][1]:
            return -1
        if (scores[idx][0] + scores[idx][1]) < ho_sum_score:
            rank += 1

    return rank

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))