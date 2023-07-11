# 2477. 참외밭
# https://www.acmicpc.net/problem/2477

k = int(input())


ds = []  # 방향을 저장할 리스트
vs = []  # 값을 저장할 리스트
for _ in range(6):
    d, v = map(int, input().split())
    ds.append(d)
    vs.append(v)

max_idx = vs.index(max(vs))  # 가장 긴 변의 인덱스

ds = ds[max_idx:] + ds[:max_idx]  # 가장 긴 변부터 시작하도록 정렬
vs = vs[max_idx:] + vs[:max_idx]

cnt = [0] * 5
# 반복되는 위치 찾기
for idx, value in enumerate(ds):
    cnt[value] += 1
    if cnt[value] >= 2:
        start_idx = idx  # start_idx = 4

m = {0, 1, 2, 3, 4, 5} - {0, start_idx, start_idx - 1, start_idx - 2, start_idx - 3}
print((vs[0] * vs[list(m)[0]] - vs[start_idx - 1] * vs[start_idx - 2]) * k)
