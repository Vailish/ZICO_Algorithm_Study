T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')

    # N, M 값, 파리판 받아오기
    N, M = map(int, input().split())
    monster = [list(map(int, input().split())) for _ in range(N)]

    # 최종값 설정
    highest_kill = 0

    # 파리채로 쳤을때의 모든 위치의 값을 합해서 가장 큰 값을 최종값에 입력
    for k_start_i in range(N - M + 1):
        for k_start_j in range(N - M + 1):
            kill_count = 0
            for i in range(M):
                for j in range(M):
                    kill_count += monster[k_start_i + i][k_start_j + j]
            if kill_count > highest_kill:
                highest_kill = kill_count

    # 최종값 출력
    print(highest_kill)
