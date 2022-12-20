# 2578 빙고
arr = [list(map(int, input().split())) for _ in range(5)]
cnt_call = 0  # 사회자가 부른 수
a = True
while a:
    for x in range(5):
        for num in input().split():
            num = int(num)
            if a:
                cnt_call += 1  # 사회자
                for n in range(5):
                    if num in arr[n]:
                        y = arr[n].index(num)
                        arr[n][y] = 0  # 부른 수 검사
                    cnt = 0
                    temp_sum_down = 0
                    temp_sum_up = 0

                    for i in range(5):  # 빙고 검사
                        if sum(arr[i]) == 0:  # 가로 검사
                            cnt += 1
                        temp_sum_down += arr[i][i]
                        temp_sum_up += arr[i][-i -1]
                    if temp_sum_down == 0: # 하향 대각 검사
                        cnt += 1
                    if temp_sum_up == 0: # 상향 대각 검사
                        cnt += 1
                    for j in range(5):  # 세로 검사
                        temp_sum = 0
                        for i in range(5):
                            temp_sum += arr[i][j]
                        if temp_sum == 0:
                            cnt += 1
                    if cnt >= 3:
                        a = False
                        break
print(f'{cnt_call}')