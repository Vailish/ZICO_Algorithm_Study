for test_case in range(1,int(input())+1):
    sentence = input()

    for repeat_len in range(1,11):                  # 반복문자 길이는 1~10. 제일 적은 길이가 답
        temp = sentence[:repeat_len] * 30           # 여유롭게 *30 (길이가 1일때도 대비)
        temp = temp[:30]                            # 30개만 슬라이스 (temp도 30글자, 문장도 30글자)
        if sentence == temp:                        # 이 둘이 같다면, 현재 반복문자 길이가 옳바른것
            print(f'#{test_case} {repeat_len}')
            break

# 문제에 설명이 부족한부분
# 1. 반복마디중 제일 작은길이 출력 (ex: aaaaa 의 경우, 1~5 전부 마디가 될 수 있지만 1 출력)
# 2. 마디가 반복되다가 문자열의 끝에서 잘리는 경우 (ex: aabbb aabbb aabb) 잘린 문자열은 마디의 앞부분과 일치하기만 하면 됨, 이 경우 5 출력