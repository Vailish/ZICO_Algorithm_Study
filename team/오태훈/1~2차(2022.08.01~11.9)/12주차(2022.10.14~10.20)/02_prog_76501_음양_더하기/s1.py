def solution(absolutes, signs):
    result = 0
    for i in range(len(signs)):
        if signs[i]:
            result += absolutes[i]
        else:
            result -= absolutes[i]
    return result



print(solution([4,7,12], [true,false,true]))