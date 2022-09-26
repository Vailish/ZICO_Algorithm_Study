n, k = map(int, input().split())
people = [[0] * 2 for _ in range(7)]    # [여학생 수, 남학생 수] 인덱스는 학년
result = 0
for _ in range(n):
    s, y = map(int, input().split())
    people[y][s] += 1
for i in range(1, 7):
    for j in range(2):
        if people[i][j] % k:
            result += (people[i][j] // k + 1)
        else:
            result += people[i][j] // k
print(result)
