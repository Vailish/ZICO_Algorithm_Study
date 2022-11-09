# boj_16235 나무 재테크 골드3
# https://www.acmicpc.net/problem/16235

# 양분 default값 5
# 봄 : 자신의 나이만큼 양분을 먹음 -> 나이 +1, 가장 나이가 어린 나무부터 양분 먹음, 못 먹을시 죽음
# 여름 : 죽은나무 나이//2 양분이 됨
# 가을 : 나무 나이 5의 배수 -> 인접한 8칸에 나이가 1인 나무 생성, 상도의 땅 안에서만
# 겨울 : 양분 투척 -> fertilizer
def solution(planting_trees):
    trees = [[[] for _ in range(N)] for _ in range(N)]
    # 기본 필드에 나무 심어주기
    for x, y, a in planting_trees:
        trees[x-1][y-1].append(a)  # (1, 1)부터 시작하기 때문
    for year in range(K):
        # 봄
        dead_trees = []  # 죽은 나무, (x, y, 나이)
        live_trees = [[[] for _ in range(N)] for _ in range(N)]
        plus_trees = []
        for i in range(N):
            for j in range(N):
                if trees[i][j]:
                    for n in range(len(trees[i][j]) - 1, - 1, - 1):  # 우측에 아기나무를 붙일거기 때문에 뒤집어서 진행
                        if field[i][j] >= trees[i][j][n]:
                            field[i][j] -= trees[i][j][n]
                            live_trees[i][j].append(trees[i][j][n] + 1)
                            if not (trees[i][j][n]+1) % 5:
                                plus_trees.append((i, j))

                        else:
                            dead_trees.append([i, j, trees[i][j][n]])

        # 여름
        for r, c, age in dead_trees:
            fertilizer[r][c] += age//2

        # 가을
        for r, c in plus_trees:
            for direction in range(8):
                # 상 하 좌 우 우상 우하 좌상 좌하
                nr = r + [-1, 1, 0, 0, -1, 1, -1, 1][direction]
                nc = c + [0, 0, -1, 1, 1, 1, -1, -1][direction]
                if 0 <= nr < N and 0 <= nc < N:
                    live_trees[nr][nc].append(1)

        # 겨울
        for i in range(N):
            for j in range(N):
                field[i][j] += fertilizer[i][j]
        trees = live_trees[:]

    answer = 0
    for i in range(N):
        for j in range(N):
            answer += len(live_trees[i][j])
    return answer


N, M, K = map(int, input().split())  # N = 땅크기, M = 초기 나무 수, K = 경과 기간
fertilizer = [list(map(int, input().split())) for _ in range(N)]  # 겨울에 주는 영양분의 양

planting_trees = []
for _ in range(M):
    p, q, tree_age = map(int, input().split())
    planting_trees.append([p-1, q-1, tree_age])

field = [[5] * N for _ in range(N)]  # 현재 땅의 영양도

# 그냥 [[[]] * N for _ in range(N)] 이런식으로 쓰면 얕은 복사가 일어나서 하나만 append하더라도 한 번에 한줄 다 들어감
# trees = [[[] for _ in range(N)] for _ in range(N)]

planting_trees = sorted(planting_trees, key=lambda x: x[2])
print(solution(planting_trees))

'''
2, 1, 3
3, 2, 3
N = 5
[[[], [], [], [], 3],
[3, [], [], [], []], 
[[], [], [], [], []], 
[[], [], [], [], []], 
[[], [], [], [], []]]
'''