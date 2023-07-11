def solution(book_time):
    book_time.sort()  # 시작순으로 정렬
    queue = book_time[1:]
    space = [book_time[0]]
    start, end = space[-1]
    standard_time = int(end[:2]) * 60 + int(end[3:])
    while queue:
        target_start_time, target_end_time = queue.pop(0)

        target_time = int(target_start_time[:2]) * 60 + int(target_start_time[3:])

        if target_time < standard_time + 10:
            space.append([target_start_time, target_end_time])

            standard_time = int(target_end_time[:2]) * 60 + int(target_end_time[3:])
        print("#####################")
        print(space)
        print("standardtime : " + str(standard_time))
        print("#####################")

    return len(space)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
