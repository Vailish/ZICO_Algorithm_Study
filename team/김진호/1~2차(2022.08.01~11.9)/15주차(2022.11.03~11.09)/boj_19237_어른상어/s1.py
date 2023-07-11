di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

# 1. 상어의 이동 처리
def shark_move():
    cnt = 0
    while cnt <= 1000 and len(sharkes) > 1:         # 상어의 이동이 1000회를 넘거나, 한마리가 남으면 종료
        # temp = set()
        left_shark = []                                   # 살아남은 상어를 담을 left_shark 배열
        visited = set()                                   # 순위가 높은 상어가 방문한 위치를 담을 set
        while sharkes:
            pos, rank, Dir = sharkes.pop(0)
            last_choice = []                              # 모든 방향이 가로막혀 있을때 결정할 자신 냄새가 있는 칸을 담을 배열
            for p in dir_priority[rank][Dir]:             # 현재 순위의 상어가 바라보는 방향에 따라서 순차적으로 주변 4방향 바라보기
                dx = pos[0] + di[p]
                dy = pos[1] + dj[p]
                if 0 <= dx < N and 0 <= dy < N and not sharkes_maps[dx][dy]:    # 바라보는 위치에 냄새 흔적이 없다면
                    if (dx, dy) not in visited:                                 # (1) 이전에 방문한적없다 == 이동해도 상어가 살아 남는다
                        # temp.add(((dx, dy), rank, p))
                        left_shark.append(((dx, dy), rank, p))                  #     해당 칸으로 이동한 상어의 정보를 left_shark에 임시로 저장
                        visited.add((dx, dy))                                   #     방문 처리 및 break
                        break
                    else:                                                       # (2) 이전에 방문한적이 있다 == 이동하면 반드시 상어가 죽는다
                        break                                                   #     상어의 정보를 넣지않고 break
                elif 0 <= dx < N and 0 <= dy < N and sharkes_maps[dx][dy] and sharkes_maps[dx][dy][0] == rank and not last_choice:
                                                                                # 모든 4방향에 막혀있는 경우를 위하여, 바라보는 위치의 냄새가
                                                                                # 현재 상어의 냄새이고, 이것이 우선순위에 따라 첫 위치라면
                                                                                # 해당 위치값을 last_choice에 넣어준다
                    last_choice = [dx,dy,p]
            else:                                                                           # 4방향이 모두 냄새가 이미 있거나, 막혀있을때
                # temp.add(((last_choice[0], last_choice[1]), rank, last_choice[2]))
                left_shark.append(((last_choice[0], last_choice[1]), rank, last_choice[2])) # 위에서 구한 우선순위에 따른 자신의 냄새가 있는 칸으로 이동
                visited.add((last_choice[0], last_choice[1]))                               # 방문처리
        time_pass()                         # 각 냄새의 시간 -1처리
        for shark in left_shark:            # 상어 재배치, 냄새남기기
            pos, rank, Dir = shark
            sharkes.append(shark)
            sharkes_maps[pos[0]][pos[1]] = [rank, K]
        # 기본적으로 set, list는 Iterable하지만 set은 index가 없기때문에 순서가 존재하지않는다.
        # 따라서 출력에서는 set이 순서대로 뽑히는것처럼 보이지만, 각 버전에 따라서 pop처럼 랜덤으로 뽑힐 수 있다.
        # 따라서 되도록 순서가 필요한 for문에서는 dict나 set같은 순서없는 자료형을 쓰지말자.
        cnt += 1
    return cnt

# 2. 상어의 냄새 시간처리
def time_pass():
    for i in range(N):
        for j in range(N):
            if sharkes_maps[i][j]:              # 해당 위치에 값이 있다 == 이전에 생성된 냄새가 있다
                sharkes_maps[i][j][1] -= 1      # 냄새의 지속시간 -1
                if sharkes_maps[i][j][1] == 0:  # 지속시간이 0이되면
                    sharkes_maps[i][j] = []     # 해당값 삭제(초기화)

# 0. 기본값 받기
N, M, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
sharkes_maps = [[[] for _ in range(N)] for _ in range(N)]  # 초기 maps가 아닌 새로운 maps에 냄새 정보를 입력한다
sharkes_pos = [0] + list(map(int, input().split()))        # 상어의 초기 방향 입력받기(맨앞 0은 추출이 편하도록 추가)
sharkes = []                                               # 상어의 위치, 순위, 방향을 담을 배열

# 0_1. 기본값을 문제풀이에 적합한 형태로 전환
for i in range(N):
    for j in range(N):
        if maps[i][j]:                                                      # 상어가 있는 칸이라면
            sharkes.append(((i, j), maps[i][j], sharkes_pos[maps[i][j]]))   # 위치,순위,방향을 sharker에 담아준다
            sharkes_maps[i][j] = [maps[i][j], K]                            # 새로운 maps에 냄새를 남기는 상어 순위와 초기 냄새 지속시간을 담는다
sharkes.sort(key=lambda x: x[1])                                            # 이후 계산이 편하도록 순위가 낮은 상어->높은 상어 순서대로 뽑히도록 sort
dir_priority = {}                                                           # 상어의 방향 우선순위를 담을 딕셔너리 생성
for m in range(1, M + 1):
    dir_priority[m] = [0] + [list(map(int, input().split())) for _ in range(4)]  # 딕셔너리[상어순위][현재바라보는위치] 형식으로 방향 우선순위를 받는다
result = shark_move()                                                            # 상어들의 이동 처리하는 shark_move() 함수호출 및 return값 받기
if result == 1001:                                                          # 1000회 반복이 초과하면 -1로 치환
    result = -1
print(result)
