def sol():
    def stack():
        # 만약 체크할 것이 없으면 0 반환
        if not chk_list:
            return 0

        # chk_list를 내림차순으로 정렬 왜냐 list.pop()를 사용할 것이기 때문에
        # deque를 import하지 않고 뒤에서부터 값을 빼와서 사용할 것이여서 시간이득을 위하여
        chk_list.sort(reverse=True)

        # 거리, x번째 원자, y번째 원자 초기값 세팅
        distance, x, y = chk_list.pop()

        # answer는 폭발하는 원자의 용량을 넣어줄 것인데
        # 초기값을 x번째와 y번째가 폭발하는 것을 기준으로 세팅
        answer = atom_list[x][3] + atom_list[y][3]

        # 사용한 원자를 확인하기 위해 초기값 x, y를 넣은 chk 함수 세팅
        chk = {x, y}

        # chk_list가 빌 때까지 반복
        while chk_list:
            # 거리, x번째 원자, y번째 원자 빼오기
            d, x, y = chk_list.pop()

            # 만약 x와 y가 둘 다 사용한 원자가 아니라면
            if x not in chk and y not in chk:
                # 초기값 바꿔주고 두 원자의 용량을 모두 answer에 추가
                distance = d
                answer += atom_list[x][3] + atom_list[y][3]
                chk.update((x, y))

            # 만약 거리가 이전에 확인했던 거리와 같다면
            # 거리를 기준으로 내림차순 정렬을 했기 때문에 뒤에서부터 빼오는 d는 오름차순으로 나온다
            # 그래서 폭발하는 원자의 쌍 중에 가장 거리가 작은 것부터 확인하는데
            # 만약 빼오는 x번째 y번째 원자 중 하나라도 사용한 적이 있으면
            # distance에는 x나 y번째의 원자가 폭발할 수 있었던 것들 중 최소 거리가 저장된다
            # 고로 distance가 d와 같지 않으면 두 원자 중 하나는 앞에서 다른 원자와 폭발하기 때문에
            # 해당하는 원자들은 폭발하지 않는다
            elif distance == d:
                # x를 사용하지 않았으면 x의 용량을 answer에 추가
                if x not in chk:
                    answer += atom_list[x][3]
                    chk.add(x)
                # y를 사용하지 않았으면 y의 용량을 answer에 추가
                if y not in chk:
                    answer += atom_list[y][3]
                    chk.add(y)
        return answer

    # 여기서 반복 시작
    for tc in range(1, int(input()) + 1):

        # input 받아오기
        n = int(input())
        atom_list = [list(map(int, input().split())) for _ in range(n)]

        # 원자 위치 리스트를 오름차순으로 정렬
        # 다만 첫번째를 기준으로 정렬하기 때문에 x좌표를 기준으로 오름차순 정렬
        atom_list.sort()

        # 해당하는 원자와 폭발 가능한 원자를 저장할 리스트
        # 리스트에 넣을 것은 (거리, i번째, j번째)
        chk_list = []

        # 원자 반복
        for i in range(n - 1):
            for j in range(i + 1, n):
                # x 좌표의 차와 y 좌표의 차를 저장
                dx = atom_list[i][0] - atom_list[j][0]
                dy = atom_list[i][1] - atom_list[j][1]

                # y 좌표의 차가 0이면
                if dy == 0:
                    # i번째 원자의 방향이 우이고 j번째 원자의 방향이 좌이면 폭발가능
                    # 여기서 i번째 원자의 방향이 좌이고 j번째 원자의 방향이 우이면 폭발가능한지 확인 안 하는 이유는
                    # x 좌표를 기준으로 정렬했기 때문에 항상 i번째 원자가 j번째 원자의 왼쪽에 위치하기 때문이다.
                    # 고로 dx는 항상 음수
                    if atom_list[i][2] == 3 and atom_list[j][2] == 2:
                        chk_list.append((-dx, i, j))

                # x 좌표의 차가 0이면
                elif dx == 0:
                    # y 좌표의 차가 0보다 작고 i번째 원자의 방향이 상이고 j번째 원자의 방향이 하이면 폭발 가능
                    if (atom_list[i][2], atom_list[j][2]) == (0, 1) and dy < 0:
                        chk_list.append((-dy, i, j))
                    # y 좌표의 차가 0보다 크고 i번째 원자의 방향이 하이고 j번째 원자의 방향이 상이면 폭발 가능
                    elif (atom_list[i][2], atom_list[j][2]) == (1, 0) and dy > 0:
                        chk_list.append((dy, i, j))

                # y 좌표의 차와 x 좌표의 차가 같으면
                # 위에서와 같이 dx는 무조건 음수인것을 생각하고 봐야함
                elif dx == dy:
                    # i번째 원자의 방향이 우이고 j번째 원자의 방향이 하이거나
                    # i번째 원자의 방향이 상이고 j번째 원자의 방향이 좌이면 폭발가능
                    if atom_list[i][2] == 3 and atom_list[j][2] == 1 or atom_list[i][2] == 0 and atom_list[j][2] == 2:
                        chk_list.append((abs(dx) + abs(dy), i, j))
                elif dx == -dy:
                    # i번째 원자의 방향이 우이고 j번째 원자의 방향이 상이거나
                    # i번째 원자의 방향이 하이고 j번째 원자의 방향이 좌이면 폭발가능
                    if atom_list[i][2] == 3 and atom_list[j][2] == 0 or atom_list[i][2] == 1 and atom_list[j][2] == 2:
                        chk_list.append((abs(dx) + abs(dy), i, j))
        print('#{} {}'.format(tc, stack()))


sol()
