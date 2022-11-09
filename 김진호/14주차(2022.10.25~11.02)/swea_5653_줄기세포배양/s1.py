# 번식함수
# 일단 전시간까지 방문한곳은 제외,
def breeding(pos,val):
    x, y = pos[0], pos[1]
    for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if (dx,dy) not in visited:
            visited.add((dx,dy))
            L3.append(((dx,dy),val,val))


# 1시간이 흐른뒤 세포상태.
# L1에서 모든것을 죽었는지, 확산인지, 아닌지에 따라서 각 배열 혹은 함수 호출
def timepass():
    while L1:
        pos, val, life = L1.pop()
        life -= 1
        if life == -val and val != 1:
            continue
        elif life == -1:
            breeding(pos,val)
            if val == 1:
                continue
        L2.append((pos, val, life))


for tc in range(1,int(input())+1):
    N, M, K = map(int,input().split())
    Early = [list(map(int,input().split())) for _ in range(N)]
    visited = set()
    L1 = []
    L2 = []
    L3 = []

    # 초기 데이터 정리
    for i in range(N):
        for j in range(M):
            if Early[i][j] > 0:
                L1.append(((i, j), Early[i][j], Early[i][j]))
                visited.add((i, j))
    # K횟수만큼 반복
    cnt = 0
    while K > cnt:
        L1.sort(key=lambda x: x[1])
        timepass()
        L1 = L2 + L3
        L2 = []
        L3 = []
        cnt += 1
    print(f'#{tc} {len(L1)}')
