# 스택수열 - 실버2
# https://www.acmicpc.net/problem/1874


def solution():
    stack = []
    # 1부터 하나씩 넣는다.
    # 목표 값과 비교해서 작으면 + 출력하고 스택에 넣는다. 크다면 스택에서 pop하고 - 를 출력한다. 해당값이 다르다면 NO를 출력한다
    # 목표값과 같다면 push 후 pop 한다. 즉, + 출력 후 - 출력한다
    # 계속 돌린다.
    max_num = int(input())
    n = 1
    targets = []
    for _ in range(max_num):
        targets.append(int(input()))
    index = 0

    while True:
        if n == max_num:
            return

        if n < targets[0]:
            print("+")
            stack.append(n)
            n += 1
        elif n == targets[0]:
            print("+")
            print("-")
            n += 1
        else:  # n > targets[0]
            if stack:
                print("-")
                pop_num = stack.pop
                if pop_num == targets[0]:
                    print("-")
                else:
                    print("NO")
                    return
            else:
                print("NO")
                return


solution()
