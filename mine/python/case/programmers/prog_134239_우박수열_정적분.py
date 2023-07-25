# prog 134239 lv2 우박수열 정적분
# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def solution(k, ranges):
    cnt = 0
    lst = [[0, k]]

    # 좌표 구하기
    while k != 1:  # k가 1이 아닐 경우
        cnt += 1
        if k % 2 == 0:
            k = k//2
        else:
            k = k * 3 + 1
        lst.append([cnt, k])

    areas = []
    # 넓이 저장하기(적분값 구해놓기)
    # 사다리꼴 넓이 = (윗변 + 아랫변) * 높이 / 2
    for n in range(cnt):
        areas.append((lst[n][1] + lst[n+1][1]) / 2)

    answer = []
    # 요구한 적분값 저장하기
    for value in ranges:
        start, end = value[0], len(lst) + value[1] - 1  # 불러오는 좌표가 1부터 시작이기 떄문에 길이에서 초기값을 뺴야함(-1)
        if start > end:
            answer.append(-1.0)
        elif start == end:
            answer.append(0.0)
        else:
            answer.append(sum(areas[start:end]))
    return answer


print(solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]]))  # [33.0,31.5,0.0,-1.0])
