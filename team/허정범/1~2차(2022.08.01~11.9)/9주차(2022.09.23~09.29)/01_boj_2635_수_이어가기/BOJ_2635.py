n = int(input())
result = [4]    # 두번째 수를 n 으로 뒀을 때 무조건 4개 초기화
for i in range(1, n):
    n1, n2 = n, n - i
    cnt = 2
    while True:
        if n1 >= n2:
            n1, n2 = n2, n1 - n2
            cnt += 1
        else:
            break
    if result[-1] > cnt:
        break
    result.append(cnt)

print(result[-1])
n1, n2 = n, n - (len(result) - 1)
while True:
    print(n1, end=" ")
    if n1 >= n2:
        n1, n2 = n2, n1 - n2
    else:
        print(n2)
        break