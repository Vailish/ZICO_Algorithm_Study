def solution(data):
    for start, end in range(data):
        int(start[0:2] * 60 + start[3:]), int(end[0:2] * 60 + end)
    return

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))