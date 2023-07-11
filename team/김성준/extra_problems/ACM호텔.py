# ACM 호텔
# https://www.acmicpc.net/problem/10250
# for case in range(int(input())):
#     # H : 층수, W : 방수, N : n번째 손님
#     H, W, N = map(int, input().split())
#     # 시작 점 (1, 1)
#     (r, c) = (1, 1)
#     # 호텔
#     hotel = [[0] * W for _ in range(H)]
#     print(hotel)
#     n = 1
#     while True:
#         print(r, c, n)
#         if n == N:
#             break
#         if hotel[r][c] == 0:
#             hotel[r][c] = n
#             n += 1
#
#         if r == 1:
#             r += c
#             c = 1
#             continue
#
#         nr = r - 1
#         nc = c + 1
#
#     print(str(r)+str(c))
#
#
#     # 1, 2, 4, 7
#     # 3, 5, 8,
#     # 6, 9,
#     # 10

# for _ in range(int(input())):
#     H, W, N = map(int, input().split())
#     # a = 2, b= 3 일경우 203호
#     a = N % H
#     b = N // H + 1
#     if a == 0:
#         a = H
#         b -= 1
#     print(a*100 + b)

print(3%6)