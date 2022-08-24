# 2005. 파스칼의 삼각형
def pascal(stack):
    global n
    new_stack = []
    old_num = 0
    # 파스칼의 삼각형의 맨위 1 만들기
    if not stack:
        new_stack = [1]
    # 그 다음줄부터
    else:
        # stack의 길이 +1 만큼 반복 (파스칼의 삼각형의 현재 줄 길이는 직전 줄의 길이 +1)
        for _ in range(len(stack) + 1):
            # stack이 비어있으먄 now_num = 0 (맨 마지막)
            if not stack:
                now_num = 0
            # 그 외
            else:
                now_num = stack.pop()
            # new_stack에 이전 값과 현재 값 더해주기
            new_stack.append(old_num + now_num)
            # 지금 숫자를 이전 숫자로 만들기
            old_num = now_num
    # 삼각형의 한 줄 출력
    print(*new_stack)
    # 만들고자 하는 줄까지 만들면 종료
    if len(new_stack) >= n:
        return
    # 더 만들어야 하면 재귀
    else:
        pascal(new_stack)


for t in range(1, int(input()) + 1):
    print(f'#{t}')
    n = int(input())

    stack = []
    pascal(stack)
