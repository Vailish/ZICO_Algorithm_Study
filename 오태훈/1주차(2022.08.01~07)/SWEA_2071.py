2071. 평균값 구하기
T = int(input())
 
for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
 
    avr = sum(numbers) / len(numbers)
    int_avr = round(avr)
 
    print(f'#{t} {int_avr}')