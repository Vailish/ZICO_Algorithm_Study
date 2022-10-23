# 도난 당한 학생 번호 -1, +1이 여분의 옷을 가져온 학생 번호에서 확인 한 후
# 있다면 빌리고 해당 여분 번호를 지운다.
# 없다면 전체 학생 수에서 빼준다
# 이를 반복한 뒤, 마지막에 학생 수를 출력한다.

def solution(n, lost, reserve):
    attendance = n
    lost_length = len(lost)

    # depth = 잃어버린 애 번호 reserve = 남은 여분 옷, nums = 참여자 수
    def dfs(depth, reserve, nums):
        nonlocal attendance
        # 종료조건
        if depth == lost_length:
            attendance = max(attendance, nums)
            return

        # 순회
        if lost[depth] - 1 in reserve or lost[depth] in reserve or lost[depth] + 1 in reserve:
            for i in range(3):
                if lost[depth] + (i - 1) in reserve:
                    new_reserve = reserve[:]
                    new_reserve.remove(lost[depth] + i - 1)
                    dfs(depth + 1, new_reserve, nums)
        else:
            dfs(depth + 1, reserve, nums - 1)

    dfs(0, reserve, attendance)
    return attendance

print(solution(5, [2, 4], [3]))


# def dfs(lost, reserve, can_join):
#     print(lost, reserve)
#     global allstudent
#     if not lost:
#         if can_join > allstudent:
#             allstudent = can_join
#         return
#     student = lost.pop()
#     for i in [-1, 0, 1]:
#         if student + i in reserve:
#             reserve.discard(student + i)
#             dfs(lost, reserve, can_join + 1)
#             # reserve.add(student + i)
#     dfs(lost, reserve, can_join)
#
#
# def solution(n, lost, reserve):
#     global allstudent
#     new_lost = set()
#     new_reserve = set(reserve)
#     for i in lost:
#         if i in new_reserve:
#             new_reserve.remove(i)
#         else:
#             new_lost.add(i)
#     allstudent = n - len(new_lost)
#     dfs(new_lost, new_reserve, allstudent)
#     return allstudent