# 스택수열 - 실버2
# https://www.acmicpc.net/problem/1874


def solution():
    n = int(input())
    # 1부터 n까지의 수열 생성
    lst = [i for i in range(1, n+1)]
    stack = []
    result = []
    answer = []

    # 숫자가 들어오면 해당 값이 나올때까지 lst에서 pop(0) 때려서 값을 찾음 그러면서 push하면 +를 pop하면 -를 answer에 넣음
    for _ in range(n):
        num = int(input())
        while True:
            if num == lst[0]:
                result.append(lst.pop(0))
                answer.append("+")
                answer.append("-")
                break

            elif num > lst[0]:
                stack.append(lst.pop(0))
                answer.append("+")

            else:  # num < lst[0]
                if num == stack[-1]:
                    result.append(stack.pop())
                    answer.append("-")
                elif num > stack[-1]:
                    print("NO")
                    return
                else:
                    # stack = [1, 2, 4] 인데 2가 필요하데 어떻게 할래?
                    # stack 안에 있는지 확인
                    if num in stack:
                        # num 위치를 찾아서 제거 & len(stack) - index 만큼
                        num_idx = stack.index(num)
                        answer.append("-")


                    else:
                        print("NO")
                        return


    # 모든 input 값들을 사용하게 되면 answer를 출력 불가능하다면 "NO" 출력



    return


solution()
