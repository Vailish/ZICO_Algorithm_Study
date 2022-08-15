game_369 = ['3', '6', '9']  # 3,6,9 카운트 메소드에 사용될 리스트값

for num in range(1, int(input()) + 1):
    cnt = [0, 0, 0]  # 카운트 리스트 초기화
    num_s = str(num)
    for i in range(3):
        cnt[i] = num_s.count(game_369[i])  # 3,6,9개수 각각 카운팅

    if sum(cnt) > 0:
        for i in range(3):
            print('-' * cnt[i], end='')
        print(end=' ')
    # 3,6,9가 한개라도있다면, 그 개수만큼 - 출력. 출력문형식은 문제에 맞게.
    else:
        print(num, end=' ')
