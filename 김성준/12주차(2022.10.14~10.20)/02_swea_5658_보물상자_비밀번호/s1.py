# swea_5658 보물상자 비밀번호
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo

import sys
sys.stdin = open('input.txt')


def solution():
    result = []
    point = [0, N//4, N//4 * 2, N//4 * 3, N-1]
    for _ in range(N//4):
        tmp = ''
        for n in range(4):
            if n != 3:
                value = int(lock[point[n]:point[(n+1)]], 16)
            else:  # n == 3일 때
                for p in range(point[3], N):
                    tmp += lock[p]
                for q in range(0, point[0]):
                    tmp += lock[q]
                value = int(tmp, 16)

            if value not in result:
                result.append(value)

        for i in range(5):
            point[i] += 1
    result.sort(reverse=True)
    return result[K-1]


for case in range(1, 1 + int(input())):
    N, K = map(int, input().split())  # N = 개수 , K번째로 큰 수
    lock = input()
    print(f'#{case}', solution())
