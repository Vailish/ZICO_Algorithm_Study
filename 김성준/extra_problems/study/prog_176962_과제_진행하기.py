def solution(plans):
    # 작업중인 녀석들
    working_stack = []

    # 작업이 끝난 녀석들(정답)
    answer = []

    for i in range(len(plans)):
        plans.sort(key=lambda x: cal_time(x, ["","00:00",""]))

        print(f"################# round : {i}")
        print(f'요번 녀석 : {plans[i]}')
        print(f'작업해야하는 녀석 : {working_stack}')
        print(f'완료된 녀석 : {answer}')
        # 작업중인 녀석이 없는 경우, 작업스택에 추가
        if len(working_stack) == 0:
            working_stack.append(plans[i])
            continue

        # 하나씩 빼서
        pre_plan = working_stack.pop()

        # 작업중인 녀석과 작업할 녀석의 걸리는 시간 및 시작 시간을 비교
        # 작업할 녀석의 걸리는 시간이 더 짧을 때 ->
        # 1) 완료목록에 추가
        # 2) 반복문을 통해서 남은 시간을 소모시킴
        remain_time = cal_time(pre_plan, plans[i])
        print(f"remain_time : {remain_time} vs {pre_plan[2]}")

        if remain_time + int(pre_plan[2]) < 0:  # == 작업 중인 녀석이 안 끝났다!
            answer.append(pre_plan[0])
            remain_time += int(pre_plan[2])
            print(f" 정답에 {pre_plan} 추가 {i} / {len(plans)}")

            while working_stack:
                print(f"working_stack : {working_stack}")
                pre_plan = working_stack.pop()
                remain_time -= cal_time(pre_plan, plans[i])

                if remain_time + int(pre_plan[2]) <= 0:
                    answer.append(pre_plan[0])
                    break

            working_stack.append(plans[i])

        # 작업할 녀석의 걸리는 시간이 더 긴 경우 ->
        # 1) 시간의 차이 만큼 작업중인 녀석의 'start'와 'playtime'을 대체 함
        # 2) 작업할 녀석을 작업스택에 넣어줌
        else:
            pre_plan[1] = plans[i][1]
            pre_plan[2] = int(pre_plan[2]) + remain_time
            working_stack.append(pre_plan)
            working_stack.append(plans[i])
            print("작업할 녀석이 걸리는 시간이 더김")
    # 모든 작업이 종료 후 순차적으로 저장
    print(f"남은 작업스택 : {working_stack}")
    while working_stack:
        answer.append(working_stack.pop()[0])

    return answer


def cal_time(first_time, second_time):
    time_a = int(first_time[1][0:2]) * 60 + int(first_time[1][3:5])
    time_b = int(second_time[1][0:2]) * 60 + int(second_time[1][3:5])
    return time_a - time_b  # 두 작업의 시간차


# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
