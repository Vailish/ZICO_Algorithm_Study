room_num = list(map(int, input()))
count = [0] * 10
max = 0

for n in room_num:
    count[n] += 1  # 각각 자리에 카운트값 넣기

'''
for n in room_num:
    if n == 6 or 9:
        count[6] += 1 
    else:
        count[n] += 1
'''

count[6] = (count[6] + count[9]) / 2
if count[6] != int(count[6]):  # 6,9는 서로 교환이 가능하므로 6칸에 6,9를 더하고 나눈값을 넣음
    count[6] = int(count[6]) + 1  # 홀수인경우엔 검증을 통해 정수형으로 바꾸고 1추가
count[9] = 0

''' int 형변환 안하기
if (count[6]+count[9]) % 2 == 1:
    count[6] = count[6]+count[9] // 2 +1
else:
    count[6] = (count[6]+count[9]) // 2
count[9] = 0

위에 if문 추가하면 바꿧으면
if count[6] % 2 == 1:
    count[6] = count[6] // 2 +1
else:
    count[6] = count[6] // 2
'''
for num in count:
    if max < num:
        max = num  # 최대값 찾기

# max = max(count)

'''
for idx,num in enumerate(count):
    if max < num:
        if idx == 6 or idx 9:
            count[6]+
        max = num
        temp = idx

if idx == 6 or idx == 9:
'''

print(int(max))  # 처음풀이때 float형 출력때문에 형변환. 위에 바꾼대로하면 없애도됨
