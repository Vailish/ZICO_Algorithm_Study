# 2027. 대각선 출력하기

start, end = 0, 4
 
for i in range(5):
    front, back = start * '+', end * '+'
    print(f'{(front)}#{back}')
    start += 1
    end -= 1