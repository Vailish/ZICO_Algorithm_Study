# boj17626 Four Squares - silver3
# https://www.acmicpc.net/problem/17626
#
# def solution():
#     global result, visited
#     n = int(input())
#     # n보다 작은 제곱수를 구한다.
#     lst = []
#     for i in range(1, int(n**(1/2))+1):
#         lst.append(i**2)
#     print(lst)
#     result = [0, 4]  # 개수, 차수
#     visited = []
#     chk(lst, [0], 1, n)
#     print(result[0])
#
#
# # 선택할 항목, 선택한 항목, 깊이, 목표값
# def chk(lst, selected, depth, goal):
#     # 조건을 만족하면 return
#     if sum(selected) == goal:
#         if depth == result[1]:
#             result[0] += 1
#             print(selected)
#         elif depth < result[1]:
#             result[0] = 1
#             result[1] = depth
#             print("######################################")
#             print(selected)
#     else:
#         if depth >= result[1]:
#             return
#         else:
#             for i in range(0, len(lst)):
#                 next_selected = selected[:]
#                 next_selected.append(lst[i])
#                 if next_selected not in visited:
#                     visited.append(next_selected)
#                     chk(lst, next_selected, depth + 1, goal)
#
# solution()
def solution():
    n = int(input())
    result = [float("inf")] * (n + 1)
    result[0] = 0
    result[1] = 1

    for i in range(2, n + 1):
        j = 1
        while j * j <= i:  # 해당 값보다 작은 제곱수 활용
            # i-j*j은 목표값에 제곱수를 뺀 값의 생성가능 최소값이고 +1은 제곱수 값을 추가한다는뜻
            result[i] = min(result[i], result[i - j * j] + 1)
            j += 1

    print(result[n])

solution()
