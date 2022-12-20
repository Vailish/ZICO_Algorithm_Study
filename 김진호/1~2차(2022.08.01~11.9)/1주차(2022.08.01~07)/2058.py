N = input()
Total = 0
for num in N:
    Total += int(num)  # int로 형변환하여 총합 구하기
print(Total)

'''
N = list(map(int, input()))  # 이어져있는 문자열 하나씩 int형으로 변환하여 리스트화
print(sum(N))
'''
