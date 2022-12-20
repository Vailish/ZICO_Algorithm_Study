# t = int(input())

# for test_case in range(1, t + 1):
#     numbers = map(int, input().split())
#     result = 0
#     for num in numbers:
#         if num > result:
#             result = num

#     print(f'#{test_case} {result}')


t = int(input())

for test_case in range(1, t + 1):
    numbers = map(int, input().split())

    print(f'#{test_case} {max(numbers)}')
