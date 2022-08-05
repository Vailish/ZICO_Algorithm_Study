N = int(input())
list_number = list(map(int, input().split()))
list_number.sort()
print(list_number[N // 2])
