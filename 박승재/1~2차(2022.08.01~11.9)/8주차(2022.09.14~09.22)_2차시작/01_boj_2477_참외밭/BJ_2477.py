# k = int(input())
# direction_length = []
# cnt = [0] * 5
# answer = 1
# d = '13241'
# for _ in range(6):
#     direction, length = map(int, input().split())
#     cnt[direction] += 1
#     direction_length.append((direction, length))
# direction_length.append((0, 0))
# sub_answer = direction_length[0][1] * direction_length[-2][1]
# for i in range(6):
#     if cnt[direction_length[i][0]] == 1:
#         answer *= direction_length[i][1]
#     elif str(direction_length[i][0]) + str(direction_length[i + 1][0]) in d:
#         sub_answer = direction_length[i][1] * direction_length[i + 1][1]
# print((answer - sub_answer) * k)


k = int(input())
length = [list(map(int, input().split()))[1] for _ in range(6)]
center = length.index(max(length))
front = length[(center + 1) % 6] * length[(center + 2) % 6]
end = length[center - 1] * length[center - 2]
print((front+end)*k)
