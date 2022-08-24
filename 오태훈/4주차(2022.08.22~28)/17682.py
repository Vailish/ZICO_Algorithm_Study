# 17682. [1차] 다트 게임


def solution(dartResult):
    queue_dart = list(map(str, dartResult))
    queue = []
    while queue_dart:
        v = queue_dart.pop(0)
        if v.isdigit() and queue_dart:
            v2 = queue_dart.pop(0)
            if v2.isdigit():
                queue.append(v + v2)
            else:
                queue.append(v)
                queue.append(v2)
        else:
            queue.append(v)
    result_stack = []
    while queue:
        value = queue.pop(0)

        if value.isdigit():
            value = int(value)
            squared = queue.pop(0)
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


for _ in range(10):
    print(solution(input()))
