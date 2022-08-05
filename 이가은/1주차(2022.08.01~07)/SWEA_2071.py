# 평균값 구하기

t = int(input())

for test_case in range(1, t + 1):
    numbers = list(map(int, input().split()))
    average = round(sum(numbers) / len(numbers))  # 반올림은 round~

    print(f'#{test_case} {average}')
