# 파스칼의 삼각형
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq

def pascal(N):
    pas = [1]
    print(*pas)
    for n in range(N-1):
        visit = [[n, n+1] for n in range(n+1)]   # 각 숫자에서 더해져야할곳 위치 배정
        next_pas = [0] * (n+2)                      # 다음 파스칼 크기만큼 초기화

        for idx in range(n+1):
            next_pas[visit[idx][0]] += pas[idx]
            next_pas[visit[idx][1]] += pas[idx]   # 상위 파스칼 숫자를 하위 인접한(이어진) 위치에다가 더해준다
        pas = next_pas                            # 만들어진 파스칼을 pas에 대입한다
        print(*pas)


for test_case in range(1, int(input())+1):
    print(f'#{test_case}')
    pascal(int(input()))

# N = 2
# pas       [1]
# next_pax  [0,0]
# visit     [[0,1]]
# next_pax  [1,1]
# pas       [1,1]

# N = 3
# pas       [1,1]
# next_pax  [0,0,0]
# visit     [[0,1],[1,2]]
# next_pax  [1,2,1]
# pas       [1,2,1]