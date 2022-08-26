def solution(word):
    word = list(word)
    nums = []
    while word:
        num = int(word.pop(0))
        if word[0] == '0':
            word.pop(0)
            num = 10                    # 1. 숫자추출(10까지 판정)

        op = word.pop(0)                # 2. T,D,S 추출

        if op == 'D':
            num **= 2
        elif op == 'T':
            num **= 3                   # 3. T,D,S 계산

        if word and word[0] in '*#':    # 4. 보너스가 있는지 점검
            bonus = word.pop(0)         # 5. 보너스 추출
            if bonus == '*':
                if nums:
                    nums[-1] *= 2
                num *= 2                # 6. 보너스가 *이라면 앞과 현재값에 *2
            elif bonus == '#':
                num *= -1               # 7. 보너스가 #이라면 현재값에 * -1

        nums.append(num)                # 8. 계산된 값을 nums 리스트에 넣기

    return sum(nums)                    # 9. 최종적으로 모든 리스트 더하기


a = '1S2D*3T'
print(solution(a))
print('result : 37')
a = '0S'
print(solution(a))
print('result : 9')
a = '1D2S0T'
print(solution(a))
print('result : 3')
a = '1S*2T*3S'
print(solution(a))
print('result : 23')
a = '1D#2S*3S'
print(solution(a))
print('result : 5')
a = '1T2D3D#'
print(solution(a))
print('result : -4')
a = '1D2S3T*'
print(solution(a))
print('result : 59')