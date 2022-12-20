k = int(input())
length_list = [tuple(map(int, input().split())) for _ in range(6)]
for i in range(6):
    if (
        length_list[i][0] == length_list[(i + 2) % 6][0]
        and length_list[(i + 1) % 6][0] == length_list[(i + 3) % 6][0]
    ):
        minus_area = length_list[(i + 1) % 6][1] * length_list[(i + 2) % 6][1]
        break

max_length1 = 0
max_length2 = 0
for j in range(0, 6, 2):
    if max_length1 < length_list[j][1]:
        max_length1 = length_list[j][1]
    if max_length2 < length_list[j + 1][1]:
        max_length2 = length_list[j + 1][1]

result = (max_length1 * max_length2 - minus_area) * k
print(result)
