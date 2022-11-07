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
        age[x][y] = a

    for year in range(K):
        # 봄
        dead_trees = []  # 죽은 나무, (x, y, 나이)
        for i in range(N):
            for j in range(N):
                if age[i][j]:
                    search_age = age[i][j][:]
                    for n in range(len(age[i][j])):
                        if search_age[i][j][n] != 0 and fertilizer[i][j] >= search_age[i][j][n]:
                            fertilizer[i][j] -= search_age[i][j]
                            age[i][j][n] += 1
                        else:
                            dead_trees.append((i, j, search_age[i][j][n]))
                            age.remove(search_age[i][j][n])

                # 가을을 위한 준비
                if age[i][j][n] % 5 == 0:
                    pass


        # 여름
        for x, y, a in dead_trees:
            fertilizer[x][y] += a//2

        # 가을

        # 겨울


    return









# N = 땅 정보 input의 줄 수, M =  상도가 심은 나무의 input 줄 수, K = K년 후 살아남은 나무의 수
N, M, K = int(input().split())
fertilizer = [list(map(int, input().split())) for _ in range(N)]
trees = [list(map(int, input().split())) for _ in range(M)]  # [[x, y, 나이], ...]
field = [[5] * N for _ in range(N)]  # 영양분 필드
age = [[0] * N for _ in range(N)]  # 나무나이 필드[[[나무1, 나무2, ...], [], ...], ...]

print(solution())
