di = [0,-1,0,1]
dj = [-1,0,1,0] # 시계   좌상우하
vec1 = [2,0,1,3]  # 시계일때 시작위치
vec2 = [4,2,3,1]  # 반시계일때 시작위치

row, col = map(int, input().split())
shops = int(input())
pos = [list(map(int, input().split())) for _ in range(shops+1)]
dis1 = []
dis2 = []
graph_pos = []

for idx in range(shops+1):
    if pos[idx][0] == 1:
        graph_pos.append([0,pos[idx][1]])
    elif pos[idx][0] == 2:
        graph_pos.append([col,pos[idx][1]])
    elif pos[idx][0] == 3:
        graph_pos.append([pos[idx][1],0])
    elif pos[idx][0] == 4:
        graph_pos.append([pos[idx][1],row])

npc_vec = pos[-1][0]
npc_pos = graph_pos[-1]
max_move = row * 2 + col * 2
cnt = 0
while cnt != max_move:  # 시계방향
    vec = vec1[npc_vec]
    npc_pos[0] += di[vec]
    npc_pos[1] += dj[vec]
    cnt += 1
    for idx in range(shops):
        if npc_pos == graph_pos[idx]:
            dis1.append(cnt)
            break

    if npc_pos == [0,0] and npc_pos == [0,row] and npc_pos == [col,row] and npc_pos == [col,0]:
        vec = (vec + 1) % 4

cnt = 0
while cnt != max_move:  # 반시계방향
    vec = vec2[npc_vec]
    npc_pos[0] += di[vec]
    npc_pos[1] += dj[vec]
    cnt += 1
    for idx in range(shops):
        if npc_pos == graph_pos[idx]:
            dis2.append(cnt)
            break

    if npc_pos == [0, 0] and npc_pos == [0, row] and npc_pos == [col, row] and npc_pos == [col, 0]:
        if vec - 1 == -1:
            vec = 4
        else:
            vec -= 1

dis2 = dis2[::-1]
for idx in range(shops):
    if dis1[idx] > dis2[idx]:
        dis1[idx] = dis2[idx]

print(sum(dis1))