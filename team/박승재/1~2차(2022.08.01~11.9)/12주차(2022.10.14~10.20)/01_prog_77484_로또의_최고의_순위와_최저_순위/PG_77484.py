def solution(lottos, win_nums):
    cnt = 0
    cnt_num = 0
    for num in lottos:
        if num == 0:
            cnt_num += 1
        if num in win_nums:
            cnt += 1
    cnt_num += cnt
    answer = [7-cnt_num if cnt_num > 1 else 6, 7-cnt if cnt > 1 else 6]
    print(answer)
    return answer

solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])