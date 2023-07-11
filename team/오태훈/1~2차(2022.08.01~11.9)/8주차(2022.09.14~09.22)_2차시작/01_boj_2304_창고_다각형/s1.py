# 2304. 창고 다각형
# https://www.acmicpc.net/problem/2304


def chk(arr_s):
    for idx in range(len(arr_s) - 1):
        if arr_s[idx] >= arr_s[idx + 1]:
            arr_s[idx + 1] = arr_s[idx]
    return sum(arr_s)


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
end_idx = max(list(zip(*arr))[0])

storage = [0] * (end_idx + 1)

for idx, h in arr:
    storage[idx] = h

max_h = max(storage)
max_idx = storage.index(max_h)
r_max_idx = end_idx - storage[::-1].index(max_h) + 1

arr1 = storage[:max_idx]
arr2 = storage[-1 : r_max_idx - 1 : -1]
print(max_h * (r_max_idx - max_idx) + chk(arr1) + chk(arr2))
