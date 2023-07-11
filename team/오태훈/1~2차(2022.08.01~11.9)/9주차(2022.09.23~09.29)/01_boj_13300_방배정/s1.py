# 13300. 방 배정

import math

n, k = map(int, input().split())

male = [0] * 7
female = [0] * 7

for _ in range(n):
    s, y = map(int, input().split())
    # 여학생
    if s == 0:
        female[y] += 1
    # 남학생
    else:
        male[y] += 1


cnt = 0
for i in range(1, 7):
    cnt += math.ceil(female[i] / k)
    cnt += math.ceil(male[i] / k)
print(cnt)
