for test_case in range(1, int(input()) + 1):
    days = int(input())
    future = list(map(int, input().split()))
    future_temp = []
    earn = 0
    idx = 0

    future_max = max(future)
    idx_max = future.index(future_max)  # 리스트의 최대값과 인덱스 추출

    while 1:
        if idx_max != 0:
            earn += future_max * idx_max - sum(future[:idx_max])
        # 최대값이 맨앞(인덱스0)이 아니라면, 최대값 * 인덱스 - 최대값까지 더한값을 계산하여
        # 앞에있는 모든물건을 최대값에서 모두 판매할때 이윤을 계산.

        if idx_max + 1 == len(future):
            break
        else:
            future = future[idx_max + 1 :]
        # 최대값이 맨뒤에 있을때, 반복 종료
        # 아니라면 최대값 다음부터 슬라이싱

        future_max = max(future)
        idx_max = future.index(future_max)
        # 최대값 및 인덱스 재 추출

    print(f'#{test_case} {earn}')
