for t in range(1, int(input()) + 1):
    total = 0
    for i in range(int(input())+1):
        total += i if i % 2 else -i  # 홀수면 양수, 짝수면 음수값 더하기
    print(f'#{t} {total}')