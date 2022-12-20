n = int(input())
dice_info = [list(map(int, input().split())) for _ in range(n)]
pair = [5, 3, 4, 1, 2, 0]
result = 0
# 첫번째 주사위 바닥면 A~E까지 완전 탐색
for i, num in enumerate(dice_info[0]):
    t_idx = i  # 시작점을 정하가위해 0번째 주사위 top 값으로 설정
    top_num = num
    temp_sum = 0

    # 1번째 주사위부터 쌓기 시작
    for j in range(n):
        b_idx = dice_info[j].index(top_num)
        t_idx = pair[b_idx]
        top_num = dice_info[j][t_idx]

        # 옆면중 가장 큰수 찾기
        max_num = 0
        for k in range(6):
            if k != t_idx and k != b_idx:
                if max_num < dice_info[j][k]:
                    max_num = dice_info[j][k]
        temp_sum += max_num

    if result < temp_sum:
        result = temp_sum

print(result)
