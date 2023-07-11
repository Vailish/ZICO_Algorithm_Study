# prog 161989 덧칠하기

def solution(n, m, selection):
    # m > n인 경우
    if m >= n:
        return 1

    cnt = 0  # cnt = 칠한 횟수

    painted = [1] * (n+1)  # painted 칠한 곳 표시하기
    for sel in selection:
        painted[sel] = 0

    for selected in selection:
        if selected > n-m and painted[selected] == 0:  # 제일 끝에 1번에 칠하면 되는 경우
            for i in range(m):
                painted[selected-i]
            cnt += 1
            break
        if painted[selected] == 1:
            continue
        else:
            for i in range(m):
                painted[selected+i] = 1
            cnt += 1
    return cnt


print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))
