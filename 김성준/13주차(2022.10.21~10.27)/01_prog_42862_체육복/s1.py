# prog_42862 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

# 여분의 옷이 있지만, 자기 옷을 도난당한경우 여분의 옷을 빼준다.
# 도난 당한 학생 번호 -1, +1이 여분의 옷을 가져온 학생 번호에서 확인 한 후
# 있다면 빌리고 해당 여분 번호를 지운다.
# 없다면 전체 학생 수에서 빼준다
# 이를 반복한 뒤, 마지막에 학생 수를 출력한다.
def solution(n, lost, reserve):
    extras = sorted(reserve[:])
    needs = sorted(lost[:])
    attendance = n
    tmp = needs[:]
    # 본인꺼 먼저 제외
    for k in needs:
        if k in extras:
            extras.remove(k)
            tmp.remove(k)
    needs = tmp[:]

    for number in needs:
        if number - 1 in extras:
            extras.remove(number - 1)
        elif number + 1 in extras:
            extras.remove(number + 1)
        else:
            attendance -= 1
    return attendance
