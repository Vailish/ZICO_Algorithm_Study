T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')

    N = int(input())
    gain = 0
    price_list = list(map(int, input().split()))

    #  list에 아무것도 들어있지 않을 때까지 반복
    while price_list:
        #  list의 최대값 위치 찾기
        max_index = price_list.index(max(price_list))
        #  만약 최대값의 위치가 0이 아니면
        if max_index:
            #  최대값 * 최대값까지의 길이 - 최대값 이전까지의 가격의 합
            gain += max(price_list) * max_index - sum(price_list[:max_index])
            #  계산이 끝난 것들을 list에서 제거
            del price_list[:max_index]
        else:
            #  만약 최대값의 위치가 첫번째 위치일 경우 첫번째 항목 제거
            del price_list[0]
    print(gain)
