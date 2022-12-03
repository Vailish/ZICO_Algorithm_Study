from itertools import product
import sys

sys.stdin = open("input.txt")


def sol():
    def chk(times, combination):
        people1 = []
        people2 = []
        for i in range(len(times)):
            if combination[i] == 0:
                people1.append(times[i][0])
            else:
                people2.append(times[i][1])
        people1.sort()
        people2.sort()
        len1 = len(people1)
        len2 = len(people2)
        if len1 > 3:
            for i in range(len1 - 3):
                people1[i] += stairs[0][2]
        if len2 > 3:
            for i in range(len2 - 3):
                people2[i] += stairs[1][2]

        return max(people1 + people2)

    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    people = []
    stairs = []
    for i in range(n):
        for j in range(n):
            if room[i][j] == 1:
                people.append((i, j))
            elif room[i][j] > 1:
                stairs.append((i, j, room[i][j]))
    people_time = []
    for x, y in people:
        result = []
        for x1, y1, stair in stairs:
            result.append(abs(x - x1) + abs(y - y1) + stair + 1)
        people_time.append(result)
    answer = n ** n
    for comb in product([1, 0], repeat=len(people_time)):
        result = chk(people_time, comb)
        if answer > result:
            answer = result
    print(answer)


for test_case in range(1, int(input()) + 1):
    print(f'#{test_case}', end=' ')
    sol()
