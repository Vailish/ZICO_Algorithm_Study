def sol():
    # 단조 증가하는 수인지 확인
    def chk(s):
        num = s % 10
        s //= 10
        while s:
            n = s % 10
            if num < n:
                # 아니면 False 리턴
                return False
            num = n
            s //= 10
        # 맞으면 True 리턴
        return True

    for tc in range(1, int(input()) + 1):
        answer = -1
        n = int(input())
        num_list = sorted(list(map(int, input().split())))
        # 오름차순 정렬 후 큰 값을 확인하기 위해 뒤에서부터 시작
        for num in range(n - 1, -1, -1):
            for num1 in range(num - 1, -1, -1):
                number = num_list[num] * num_list[num1]
                # 곱한 값이 이미 저장된 answer보다 작으면 확인하지 않는다.
                # 왜 continue가 아닌 break냐면 큰 수에서 작은 수로 들어가는데
                # 앞에서 곱한 값이 answer보다 작으면 num1에 다음 값이 들어가도 answer보다 작기 때문이다.
                if answer >= number:
                    break
                # 만약 단조증가하는 수이면 answer에 값 입력
                # 대소비교를 하지 않는 이유는 앞에서 가지치기로 모든 answer보다 작고 단조 증가하는 수를 거르기 때문이다.
                if chk(number):
                    answer = number
        print('#{} {}'.format(tc, answer))


sol()
