n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

print(numbers[(n // 2)])  # list는 0부터 시작이니깐 2로 나눈 몫으 인덱스 설정
