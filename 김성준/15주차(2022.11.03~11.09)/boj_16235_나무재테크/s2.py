# boj_16235 나무 재테크 골드3
# https://www.acmicpc.net/problem/16235


# 양분 default값 5
# 봄 : 자신의 나이만큼 양분을 먹음 -> 나이 +1, 가장 나이가 어린 나무부터 양분 먹음, 못먹을시 죽음
# 여름 : 죽은나무 나이//2 양분이 됨
# 가을 : 나무 나이 5의 배수 -> 인접한 8칸에 나이가 1인 나무 생성, 상도의 땅 안에서만
# 겨울 : 양분 투척 -> fertilizer
def solution():
    # 기본 필드에 나무 심어주기
    for x, y, a in trees:
        print('age', age, (x, y))
        age[x][y].append(a)

    for year in range(K):
        # 봄
        dead_trees = []  # 죽은 나무, (x, y, 나이)

        for i in range(N):
            for j in range(N):
                if age[i][j]:
                    search_age = age[i][j][:]
                    increasing_tree = []
                    for n in range(len(age[i][j])):
                        if search_age[i][j[n]] != 0 and fertilizer[i][j] >= search_age[i][j][n]:
                            fertilizer[i][j] -= search_age[i][j]
                            age[i][j][n] += 1
                            # 가을을 위한 준비
                            if age[i][j][n] % 5 == 0:
                                increasing_tree.append((i, j))
                        else:
                            dead_trees.append((i, j, search_age[i][j][n]))
                            age.remove(search_age[i][j][n])

        # 여름
        for x, y, a in dead_trees:
            fertilizer[x][y] += a//2

        # 가을
        # 나무의 네 방향을 조사한 뒤 조건에 맞으면 앞에 추가
        for r, c in increasing_tree:
            # delta search
            for direction in range(8):
                # 상 하 좌 우 우상 우하 좌상 좌하
                nr = r + [-1, 1, 0, 0, -1, 1, -1, 1][direction]
                nc = c + [0, 0, -1, 1, 1, 1, -1, -1][direction]

                if 0 <= nr < N and 0 <= nc < N:
                    age[nr][nc].insert(0, 1)  # 나이가 어린 나무부터 비료를 먹으므로
        # 겨울
        for i in range(N):
            for j in range(N):
                field[i][j] += fertilizer[i][j]
    # 살아남은 총 나무 개수 구하기
    answer = 0
    for i in range(N):
        for j in range(N):
            answer += len(age[i][j])
    return answer


# N = 땅 정보 input의 줄 수, M =  상도가 심은 나무의 input 줄 수, K = K년 후 살아남은 나무의 수
N, M, K = map(int, input().split())
fertilizer = [list(map(int, input().split())) for _ in range(N)]
trees = [list(map(int, input().split())) for _ in range(M)]  # [[x, y, 나이], ...]
field = [[5] * N for _ in range(N)]  # 영양분 필드
age = [[[0]] * N for _ in range(N)]  # 나무나이 필드[[[나무1, 나무2, ...], [], ...], ...]

print(solution())
