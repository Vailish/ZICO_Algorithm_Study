# 수열 실버3
# https://www.acmicpc.net/problem/2559

import sys

N, K = list(map(int, sys.stdin.readline().split()))  # N = 전체 일 수, K = 연속된 검사 일 수
lst = list(map(int, sys.stdin.readline().split()))  # lst = 온도를 담은 리스트

# slicing window를 사용하자!!
# slicing window란 박스의 값을 미리 구한 뒤,
# 한 칸씩 박스를 옮기면서 벗어난 앞의 박스값은 빼주고
# 새로 들어온 값은 더해주는 식으로 구하는 방법을 말함!

slicing_window = sum(lst[:K])
temp = 0
result = 0
# 검사
for num in range(1, N-K+1):
    temp = - lst[num-1] + slicing_window + lst[num+1]
    if result < temp:
        result = temp
print(result)


# 검사
# max_temp = 0
# for day in range(N-K+1):
#     temp = 0
#     for num in range(day, day + K):
#         temp += lst[num]
#     if max_temp < temp:
#         max_temp = temp
# print(max_temp)