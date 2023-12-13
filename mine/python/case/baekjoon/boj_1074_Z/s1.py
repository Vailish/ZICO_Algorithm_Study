# Z - silver1
# https://www.acmicpc.net/problem/1074

# 메모리초과 -> 좌표만 구하는걸로 변경
# # 먼저 수를 채운 다음, 해당 좌표의 값을 구한다.
# # 수를 채우는 방법은 다음과 같이 구한다
# # N=1일때 4개를 채우는 함수를 생성한다.
# # N이 1이 아닐때, 각 값을 1/4하여 재귀시켜 세부적으로 나눌 수 있게 한다.
# # 재귀시 값은 우측 하단 점을 기준으로 보낸다.(0부분이 애매하기때문에)
# import sys
# sys.setrecursionlimit(3000)
#
#
# def solution():
#     def func(x, y, d):
#         nonlocal num
#         if d == 1:
#             for dx, dy in [(-1, -1), (-1, 0), (0, -1), (0, 0)]:
#                 field[x + dx - 1][y + dy - 1] = num
#                 num += 1
#         else:
#             c = 2**(d-1)
#             #우측 하단 점이 기준점이므로 상단으로 올린다고 생각
#             func(x-c, y-c, d-1)
#             func(x-c, y, d-1)
#             func(x, y-c, d-1)
#             func(x, y, d-1)
#
#     N, r, c = map(int, input().split())
#     field = [[0] * 2 ** N for _ in range(2**N)]
#     num = 0
#     if N == 1:
#         print(0)
#     else:
#         func(2**N, 2**N, N)
#         print(field[r][c])

def solution():
    N, r, c = map(int,input().split())
    answer = 0
    while N > 0:
        v = 2**(N-1)
        vn = 4**(N-1)
        # 좌상인경우
        if r < v and c < v:
            answer += 0
        elif r < v and c >= v:
            answer += vn
            c -= v

        elif r >= v and c < v:
            answer += 2 * vn
            r -= v
        else:
            answer += 3 * vn
            r -= v
            c -= v
        N -= 1
    print(answer)


solution()
