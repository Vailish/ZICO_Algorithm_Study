row, col = map(int, input().split())
shops = int(input())
shop_pos = [list(map(int, input().split())) for _ in range(shops)]
npc_pos = list(map(int, input().split()))
dis = [0] * shops

for idx in range(shops):
    shop = shop_pos[idx]

    if shop[0] == npc_pos[0]:
        dis[idx] = abs(shop[1] - npc_pos[1])

    elif shop[0] == 2 and npc_pos[0] == 3:  # 남 서
        dis[idx] = col - npc_pos[1] + shop[1]
    elif shop[0] == 3 and npc_pos[0] == 2:  # 남 서
        dis[idx] = col - shop[1] + npc_pos[1]

    elif shop[0] == 1 and npc_pos[0] == 3 or shop[0] == 3 and npc_pos[0] == 1:  # 북 서
        dis[idx] = shop[1] + npc_pos[1]

    elif shop[0] == 1 and npc_pos[0] == 4:  # 북 동
        dis[idx] = npc_pos[1] + row - shop[1]
    elif shop[0] == 4 and npc_pos[0] == 1:  # 북 동
        dis[idx] = shop[1] + row - npc_pos[1]

    elif shop[0] == 2 and npc_pos[0] == 4 or shop[0] == 4 and npc_pos[0] == 2:  # 동 남
        dis[idx] = row + col - shop[1] - npc_pos[1]

    elif shop[0] == 1 and npc_pos[0] == 2 or shop[0] == 2 and npc_pos[0] == 1:  # 남 북
        if shop[1] + npc_pos[1] <= row:
            dis[idx] = col + shop[1] + npc_pos[1]
        else:
            dis[idx] = col + 2 * row - shop[1] - npc_pos[1]
    elif shop[0] == 3 and npc_pos[0] == 4 or shop[0] == 4 and npc_pos[0] == 3:  # 동 서
        if shop[1] + npc_pos[1] <= col:
            dis[idx] = row + shop[1] + npc_pos[1]
        else:
            dis[idx] = row + 2 * col - shop[1] - npc_pos[1]

print(sum(dis))