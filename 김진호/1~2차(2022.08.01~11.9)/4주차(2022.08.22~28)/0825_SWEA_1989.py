for t in range(1, int(input()) + 1):
    w = input()
    print(f'#{t} {int(w == w[::-1])}')  # 회문이면 True, 아니면 False. int로 1 혹은 0
    print(f'#{t} ', *[int(w == w[::-1]) for w in list(input().split())])  # 회문이면 True, 아니면 False. int로 1 혹은 0
