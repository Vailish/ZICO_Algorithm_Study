# 2007. 패턴 마디의 길이 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P1kNKAl8DFAUq

for case in range(1, 1 + int(input())):
    words = input()
    for num in range(1, len(words)-1):
        if words[num] == words[0] and words[num+1] == words[1]:
            break
    print(f'#{case} {num}')
