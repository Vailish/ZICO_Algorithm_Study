n = int(input())
list_a = [tuple(map(int, input().split())) for _ in range(n)]

total_length = 0
max_i, max_h = 0, 0
result = 0

for i, h in list_a:
    if total_length < i:
        total_length = i
    if max_h < h:
        max_i = i
        max_h = h

list_b = [0] * (total_length + 1)
for i, h in list_a:
    list_b[i] = h

temp = 0
for j in range(max_i + 1):
    if temp < list_b[j]:
        temp = list_b[j]
    result += temp

temp = 0
for k in range(total_length, max_i, -1):
    if temp < list_b[k]:
        temp = list_b[k]
    result += temp

print(result)
