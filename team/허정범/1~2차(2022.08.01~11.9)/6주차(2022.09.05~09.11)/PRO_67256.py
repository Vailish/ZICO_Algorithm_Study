def solution(numbers, hand):
    answer = ''
    l, r = 9, 11
    for num in numbers:
        if num in (1, 4, 7):
            l = num - 1
            answer += 'L'
        elif num in (3, 6, 9):
            r = num - 1
            answer += 'R'
        else:
            if num == 0:
                num = 11
            l_dis = abs((num - 1) // 3 - l // 3) + abs((num - 1) % 3 - l % 3)
            r_dis = abs((num - 1) // 3 - r // 3) + abs((num - 1) % 3 - r % 3)
            if l_dis < r_dis:
                l = num - 1
                answer += 'L'
            elif l_dis > r_dis:
                r = num - 1
                answer += 'R'
            else:
                if hand == 'right':
                    r = num - 1
                    answer += 'R'
                else:
                    l = num - 1
                    answer += 'L'
    return answer
