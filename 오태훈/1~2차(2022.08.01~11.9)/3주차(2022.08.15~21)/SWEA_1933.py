# 1933. 간단한 N 의 약수

number = int(input())

for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=' ')
