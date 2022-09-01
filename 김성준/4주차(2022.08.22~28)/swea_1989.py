# 1989. 초심자의 회문 검사 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PyTLqAf4DFAUq

def palindrome(words):
    return 1 if words == words[::-1] else 0


for case in range(1, 1 + int(input())):
    print(f'#{case} {palindrome(input())}')