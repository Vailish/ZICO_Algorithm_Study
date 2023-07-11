def solution(answers):
    student1 = (1, 2, 3, 4, 5)
    student2 = (2, 1, 2, 3, 2, 4, 2, 5)
    student3 = (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    result = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == student1[i % 5]:
            result[0] += 1
        if answers[i] == student2[i % 8]:
            result[1] += 1
        if answers[i] == student3[i % 10]:
            result[2] += 1
    return [i + 1 for i in range(3) if result[i] == max(result)]
