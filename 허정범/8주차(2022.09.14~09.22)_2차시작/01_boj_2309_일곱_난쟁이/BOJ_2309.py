heights = []
for _ in range(9):
    heights.append(int(input()))
heights.sort()

for i in range(1 << 9):
    value = 0
    cnt = 0
    for j in range(9):
        if i & 1 << j:
            value += heights[j]
            cnt += 1
    if cnt == 7 and value == 100:
        break

for k in range(9):
    if i & 1 << k:
        print(heights[k])
