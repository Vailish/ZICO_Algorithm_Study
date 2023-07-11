def solution(dartResult):
    dartResult = dartResult.replace("10", "e")
    num_list = []

    for char in dartResult:
        if char.isnumeric():
            num_list.append(int(char))
        elif char == "e":
            num_list.append(10)

        elif char == "D":
            num_list[-1] **= 2
        elif char == "T":
            num_list[-1] **= 3

        elif char == "*":
            if len(num_list) >= 2:
                num_list[-2] *= 2
                num_list[-1] *= 2
            else:
                num_list[-1] *= 2
        elif char == "#":
            num_list[-1] *= -1

    answer = sum(num_list)
    return answer


print(solution(input()))
