# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PmkDKAOMDFAUq

# 1. 입력을 받고 저장 후 길이가 10 이상이면 계속 잘라서 출력

for test_case in range(1,int(input())+1):
    print(f'#{test_case}')
    word = ''
    for _ in range(int(input())):
        char, act = input().split()
        word += str(char) * int(act)
        while len(word) >= 10:          # 문자가 20자까지 들어올수있어서 한번에 2줄이상 처리가 필요할때가 있음
            print(word[:10])
            word = word[10:]
    print(word)                         # 나머지 문자열 출력

