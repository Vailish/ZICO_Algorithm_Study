def solution(lottos, win_nums):
    # def chk(k):
    #     if k == 6:
    #         result.append(1)
    #     elif k == 5:
    #         result.append(2)
    #     elif k == 4:
    #         result.append(3)
    #     elif k == 3:
    #         result.append(4)
    #     elif k == 2:
    #         result.append(5)
    #     else:
    #         result.append(6)

    rank = [6, 6, 5, 4, 3, 2, 1]
    # result = []
    n = lottos.count(0)
    cnt = 0
    for number in lottos:
        if number != 0:
           if number in win_nums:
               cnt += 1
    best = cnt + n
    # chk(best)
    # chk(cnt)
    # return result
    return [rank[best], rank[cnt]]
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))