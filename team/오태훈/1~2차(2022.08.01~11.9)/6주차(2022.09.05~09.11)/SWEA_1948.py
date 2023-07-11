# 1948. 날짜 계산기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PnnU6AOsDFAUq

for t in range(1, int(input()) + 1):
    m1, d1, m2, d2 = map(int, input().split())

    table = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    result = 0

    # 같은 달인 경우
    if m1 == m2:
        result = d2 - d1 + 1
    # 다른 달인 경우
    else:
        # 사이에 있는 달들의 일을 더한다.
        for i in range(m1 + 1, m2):
            result += table[i]
        result += table[m1] - d1 + 1 + d2
    print(f'#{t} {result}')
