# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    users = len(stages)                                 # 현재 스테이지까지 도달인 유저수 구하기
    fail_percent = [[0,i] for i in range(1,N+1)]        # 키값을 [i][1]에 넣어주기
    for i in range(1,N+1):
        if users != 0:                                  # 도달한사람이 0가 아닐때만 실행
            fail_cnt = stages.count(i)                  # 실패한사람 == 스테이지에 도달한사람. 즉 count
            fail_percent[i-1][0] = fail_cnt / users     # 실패율 넣어주기
            users -= fail_cnt                           # 실패한 유저는 다음스테이지에 도달하지 못하므로, 그 수만큼 제거한다
        else:                                           # users == 0 은 더이상 이후 스테이지에 도달한사람이 없다는뜻. 즉 나머지 실패율은 0이된다.
            break                                       # 따라서 이미 기존에 [i][0]은 0이므로 더이상 계산하지않고 반복문 탈출

    fail_percent.sort(key=lambda x:(-x[0],x[1]))        # 원하는 값은 실패율이 아니라, 실패한 스테이지이기때문에 lambda로 2번 sort실행.
                                                        # 먼저 -x[0] 즉 실패율을 검증하여 내림차순으로 정렬하는데
                                                        # 만약 이 x[0]이 같다면, 그다음 x[1] 스테이지 번호로 오름차순 정렬을한다.
    for i in fail_percent:
        answer.append(i[1])                             # 필요한 값은 스테이지이므로 스테이지값이 들어있는 [i][1]만 추출

    return answer                                       # 추출된 answer 출력

    # return sorted(result, key=lambda x : result[x], reverse=True)  # 딕셔너리 활용시 위의 3줄코딩을 한줄로 줄일수있다

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print([3,4,2,1,5])
print()
print(solution(4, [4,4,4,4,4]))
print([4,1,2,3])