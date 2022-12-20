import sys

sys.stdin = open('input.txt')


def sol():
    def dfs(num):
        if num == n:
            return True

        t, l = pakit_list[num]

        visit_cpu_queue = [0] * cpu
        for i in range(cpu):
            visit_cpu_queue[i] = max(0, cpu_queue[i] - t)

        visit_num_queue = tuple([num] + sorted(visit_cpu_queue))
        if visit_num_queue in visit:
            return False
        visit.add(visit_num_queue)

        for i in range(cpu):
            if cpu_queue[i] <= t:
                old_cpu_queue = cpu_queue[i]
                cpu_queue[i] = t + l
                if dfs(num + 1):
                    return True
                cpu_queue[i] = old_cpu_queue
            else:
                if cpu_queue[i] - t + l <= 10:
                    cpu_queue[i] += l
                    if dfs(num + 1):
                        return True
                    cpu_queue[i] -= l
        return False

    for tc in range(1, int(input()) + 1):
        n = int(input())
        pakit_list = [list(map(int, input().split())) for _ in range(n)]
        answer = -1
        for cpu in range(1, 6):
            visit = set()
            cpu_queue = [0] * cpu
            if dfs(0):
                answer = cpu
                break
        print(f'#{tc} {answer}')


sol()
