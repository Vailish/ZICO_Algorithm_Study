# BJ_1475 방 번호

N = input()
N = N.replace('9', '6')

arr = [1, 1, 1, 1, 1, 1, 2, 1, 1]
count = 1
for str_number in N:
    number = int(str_number)
    arr[number] -= 1
    # 새로운 세트를 산다.
    if arr[number] < 0:
        count += 1
        for i in range(9):
            arr[i] += 1
        arr[6] += 1

print(count)
