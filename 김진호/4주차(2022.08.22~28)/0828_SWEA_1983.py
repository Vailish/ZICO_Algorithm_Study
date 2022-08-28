for test_case in range(1,int(input())+1):
    N, K = map(int, input().split())
    score = [0] * N
    for idx in range(N):
        mid, end, hw = map(int, input().split())
        score[idx] = mid * 0.35 + end * 0.45 + hw * 0.2     # 총점 계산
    sort_score = sorted(score,reverse=True)                 # 순위를 알기위한 sort
    rank = sort_score.index(score[K-1]) // (N // 10)        # N값이 10단위로 변경되므로, rank를 10명일때처럼 0~9로 만들어주기

    print(f'#{test_case}',['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0'][rank])  # 0~9위에 따라 성적 출력