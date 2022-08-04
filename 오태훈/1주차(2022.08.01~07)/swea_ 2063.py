# 2063. 중간값 찾기

N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

middle_index = N // 2
middle_number = numbers[middle_index]
print(middle_number)
