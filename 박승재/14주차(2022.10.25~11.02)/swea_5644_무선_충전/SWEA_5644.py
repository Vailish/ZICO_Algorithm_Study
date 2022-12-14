def sol():
    def move(d):
        location_a[0] = location_a[0] + dx[moves_a[d]]
        location_a[1] = location_a[1] + dy[moves_a[d]]
        location_b[0] = location_b[0] + dx[moves_b[d]]
        location_b[1] = location_b[1] + dy[moves_b[d]]

    def find_charger():
        c_a = []
        c_b = []
        for j in range(a):
            if charger[j][2] >= abs(location_a[0] - charger[j][0]) + abs(
                location_a[1] - charger[j][1]
            ):
                c_a.append((charger[j][3], j))
            if charger[j][2] >= abs(location_b[0] - charger[j][0]) + abs(
                location_b[1] - charger[j][1]
            ):
                c_b.append((charger[j][3], j))
        c_a.sort(reverse=True)
        c_b.sort(reverse=True)
        return c_a, c_b

    def chk(li_1, li_2):
        if li_1[0][1] != li_2[0][1]:
            return li_1[0][0] + li_2[0][0]
        if len(li_1) == 1 and len(li_2) == 1:
            return li_1[0][0]
        elif len(li_1) > 1 and len(li_2) == 1:
            return li_1[1][0] + li_2[0][0]
        elif len(li_1) == 1 and len(li_2) > 1:
            return li_1[0][0] + li_2[1][0]
        else:
            return li_1[0][0] + max(li_1[1][0], li_2[1][0])

    for tc in range(1, int(input()) + 1):
        charger = []
        m, a = map(int, input().split())

        moves_a = [0] + list(map(int, input().split()))
        moves_b = [0] + list(map(int, input().split()))
        location_a = [1, 1]
        location_b = [10, 10]
        dx = [0, 0, 1, 0, -1]
        dy = [0, -1, 0, 1, 0]

        for _ in range(a):
            x, y, c, p = map(int, input().split())
            charger.append((x, y, c, p))
        answer = 0
        for i in range(m + 1):
            move(i)
            charge_a, charge_b = find_charger()
            if charge_a and charge_b:
                answer += chk(charge_a, charge_b)
            elif charge_a:
                answer += charge_a[0][0]
            elif charge_b:
                answer += charge_b[0][0]

        print('#{} {}'.format(tc, answer))


sol()
