bing_go = [list(map(int, input().split())) for _ in range(5)]
bing_go_answer = [list(map(int, input().split())) for _ in range(5)]

call_num = 0
final_result = 0
while call_num < 25:
    for i in range(5):
        for j in range(5):
            if bing_go[i][j] == bing_go_answer[call_num // 5][call_num % 5]:
                bing_go[i][j] = 0
    call_num += 1
    if call_num >= 12 and not final_result:
        bing_go_cnt = 0
        cross_cnt_1 = 0
        cross_cnt_2 = 0
        for i in range(5):
            if not sum(bing_go[i]):  # 행검사
                bing_go_cnt += 1
            if not sum(list(zip(*bing_go))[i]):  # 열검사
                bing_go_cnt += 1
            if not bing_go[i][i]:  # 좌상에서 우하단 한줄검사
                cross_cnt_1 += 1
            if not bing_go[i][-(i + 1)]:  # 좌하에서 우상 한줄검사
                cross_cnt_2 += 1

        if cross_cnt_1 == 5:
            bing_go_cnt += 1
        if cross_cnt_2 == 5:
            bing_go_cnt += 1

        if bing_go_cnt >= 3:
            final_result = call_num
            break
print(final_result)
