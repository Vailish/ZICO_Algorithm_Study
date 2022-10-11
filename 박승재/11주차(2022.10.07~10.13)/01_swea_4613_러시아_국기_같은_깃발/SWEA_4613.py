def sol():
    for tc in range(1, int(input()) + 1):
        # input 받아오기
        n, m = map(int, input().split())
        board = [input() for _ in range(n)]
        # answer = 0으로 세팅 (위치에 맞는 문자들의 개수를 셀 예정)
        answer = 0
        # W가 위치할 행 (B와 R이 적어도 한줄씩은 있어야 하니 두줄 남겨놓고 확인)
        for i in range(n - 2):
            # B가 위치할 행 (R이 적어도 한줄은 있어야 하니 한줄 남겨놓고 확인)
            for j in range(i + 1, n - 1):
                # 중간값 result 세팅
                result = 0
                for k in range(n):
                    # 안 바꿔도 되는 문자들 세기
                    # W가 위치해야 할 행
                    if k <= i:
                        result += board[k].count('W')
                    # B가 위치해야 할 행
                    elif k <= j:
                        result += board[k].count('B')
                    # R이 위치해야 할 행
                    else:
                        result += board[k].count('R')
                # 안 바꿔도 되는 문자가 많은 수를 저장
                answer = max(answer, result)
        # 출력에서 (모든 문자의 수 - 안 바꿔도 되는 문자의 수)를 출력
        print('#{} {}'.format(tc, n * m - answer))


sol()
