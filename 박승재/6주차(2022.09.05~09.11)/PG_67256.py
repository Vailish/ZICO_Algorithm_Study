def solution(numbers, hand):
    l = (1, 4, 7, '*')
    r = (3, 6, 9, '#')
    c = (2, 5, 8, 0)
    l_position = (1, 3)
    r_position = (3, 3)
    answer = ''
    for num in numbers:
        if num in l:
            answer += 'L'
            l_position = (1, l.index(num))
        elif num in r:
            answer += 'R'
            r_position = (3, r.index(num))
        else:
            c_position = (2, c.index(num))
            l_d = abs(l_position[0] - c_position[0]) + abs(l_position[1] - c_position[1])
            r_d = abs(r_position[0] - c_position[0]) + abs(r_position[1] - c_position[1])
            if l_d < r_d or l_d == r_d and hand == "left":
                answer += 'L'
                l_position = c_position[:]
            else:
                answer += 'R'
                r_position = c_position[:]
    return answer
