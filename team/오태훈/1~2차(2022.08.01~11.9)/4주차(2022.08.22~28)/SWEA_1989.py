# 1989. 초심자의 회문 검사

for t in range(1, int(input()) + 1):
    text = input()
    print(f'#{t} 1') if text == text[::-1] else print(f'#{t} 0')
