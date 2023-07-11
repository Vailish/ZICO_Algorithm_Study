# for t in range(1, int(input()) + 1):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     # 선택정렬 활용
#     for i in range(n - 1):
#         min_num = 50
#         for idx in range(i, n):
#             if min_num > arr[idx]:
#                 min_num, min_idx = arr[idx], idx
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     print(f'#{t}', end=' ')
#     print(*arr)

for t in range(1, int(input()) + 1):
    n = int(input())
    print(f'#{t}', *sorted(list(map(int, input().split()))))
