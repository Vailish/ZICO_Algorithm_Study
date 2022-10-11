def sol():
    for tc in range(1, int(input()) + 1):
        # input 받아오기
        n, m, k = map(int, input().split())
        # 도착시간을 오름차순으로 정렬
        arrive = sorted(list(map(int, input().split())))
        # 만드는 초기 시간 세팅
        make = 0
        # result 초기값을 Possible로 세팅
        result = 'Possible'
        for i in range(n):
            # k번 반복이 되면 만드는 시간에 m을 추가
            if i % k == 0:
                make += m
            # 손님 도착 시간이 만드는 시간보다 빠르면 result를 Impossible로 바꾸고 break
            if arrive[i] < make:
                result = 'Impossible'
                break
        print(f'#{tc} {result}')


sol()
