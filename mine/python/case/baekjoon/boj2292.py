# BOJ2292 벌집

input_num = int(input())
lst = [0, 1]
cnt = 1

while input_num > lst[-1]:
    cnt += 1
    lst.append(lst[-1] + (cnt-1) * 6)
print(cnt)