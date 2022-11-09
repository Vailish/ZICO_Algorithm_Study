# boj_16235 나무 재테크 골드3
# https://www.acmicpc.net/problem/16235


# 봄 : 자신의 나이만큼 양분을 먹음 -> 나이 +1, 가장 나이가 어린 나무부터 양분 먹음, 못먹을시 죽음
# 여름 : 죽은나무 나이//2 양분이 됨
# 가을 : 나무 나이 5의 배수 -> 인접한 8칸에 나이가 1인 나무 생성, 상도의 땅 안에서만
# 겨울 : 양분 투척 -> fertilizer

# 나무개체로 진행하는게 더 오래걸림... 한 블럭당 여러개의 나무가 들어갈 수 있기 때문

from collections import deque


def solution(trees):
    for year in range(1, K+1):  # 1년 ~ K년 까지
        live_trees = deque()
        plus_trees = deque()
        dead_trees = deque()
        # 봄
        for r, c, age in trees:
            if field[r][c] >= age:
                field[r][c] -= age
                live_trees.append([r, c, age+1])
                if (age+1) % 5 == 0:
                    plus_trees.append([r, c])
            else:
                dead_trees.append([r, c, age])
        
        # 여름
        for r, c, age in dead_trees:
            field[r][c] += age//2
        
        # 가을
        for r, c in plus_trees:
            for direction in range(8):
                # 상 하 좌 우 우상 우하 좌상 좌하
                nr = r + [-1, 1, 0, 0, -1, 1, -1, 1][direction]
                nc = c + [0, 0, -1, 1, 1, 1, -1, -1][direction]
                if 0 <= nr < N and 0 <= nc < N:
                    live_trees.appendleft([nr, nc, 1])
        # 겨울
        # for i in range(N):
        #     for j in range(N):
        #         field[i][j] += fertilizer[i][j]

        # for r, c, nut in nutrient:
        #     field[r][c] = nutrient
        trees = live_trees

    return len(trees)


N, M, K = map(int, input().split())  # N = 땅크기, M = 초기 나무 수, K = 경과 기간
fertilizer = [list(map(int, input().split())) for _ in range(N)]  # 겨울에 주는 영양분의 양

planting_trees = []
for _ in range(M):
    p, q, tree_age = map(int, input().split())
    planting_trees.append([p-1, q-1, tree_age])

field = [[5] * N for _ in range(N)]  # 현재 땅의 영양도
# refill = []  # 영양분 조작이 필요한 공간

planting_trees = sorted(planting_trees, key=lambda x: x[2])
print(solution(planting_trees))
