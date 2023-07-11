# 창고 다각형 실버2
# https://www.acmicpc.net/problem/2304

N = int(input())  # N = 기둥의 수
pillars = [list(map(int, input().split())) for _ in range(N)]  # H 높이, L 위치
pillars.sort(key = lambda x : x[1], reverse=1)
# 최대 기둥 높이 및 넓이
max_l, max_h = pillars.pop(0)
left = max_l
right = max_l
result = max_h  # 넓이
# 넓이 구하기
for l, h in pillars:
    if l < max_l:  # 최대 기둥 왼쪽일 때
        if l <= left:
            result += (left - l) * h
            left = l
    else:  # 최대 기둥 오른쪽일 때
        if l >= right:
            result += (l - right) * h
            right = l
print(result)