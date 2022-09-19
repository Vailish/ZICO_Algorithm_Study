# 17682. [1차] 다트 게임

# 1S2D*3T
from collections import deque


def solution(dartResult):
    queue = deque(list(map(str, dartResult)))
    squared = '0'
    result_stack = []
    while queue:
        value = queue.popleft()
        if value.isdigit():
            value = int(value)
            squared = queue.popleft()
            if squared.isdigit():
                while squared.isdigit():
                    value = int(str(value) + squared)
                    # value = 10
                    squared = queue.popleft()
            if squared == 'D':
                value = value**2
            elif squared == 'T':
                value = value**3
            result_stack.append(value)
        elif value == '*':
            pop2 = result_stack.pop()
            if result_stack:
                pop1 = result_stack.pop()
                result_stack.append(pop1 * 2)
            result_stack.append(pop2 * 2)

        elif value == '#':
            pop1 = result_stack.pop()
            result_stack.append(pop1 * -1)

    answer = sum(result_stack)

    return answer
