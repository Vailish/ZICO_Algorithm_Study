#방번호 실버5
#https://www.acmicpc.net/problem/1475

#0~9
# 6 = 9
set_num = [1, 1, 1, 1, 1, 1, 2, 1, 1]#한 세트당 숫자별 개수 0~8

room_num = list(map(int, input()))
for num in range(len(room_num)): # 9를 6으로 변환해서 합치기
    if room_num[num] == 9:
       room_num[num] = 6
# print(room_num)
room_num_counts = [0]*len(set_num)
for num in room_num : # 각각 총갯수 구하기
    room_num_counts[num] += 1

room_num_counts[6] = int(room_num_counts[6]/2 + room_num_counts[6]%2) # 나누기를 통해서 반으로 줄이되, 나머지는 더해서 올림표시

print(max(room_num_counts))