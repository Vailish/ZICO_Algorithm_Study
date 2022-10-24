# 5648. [모의 SW 역량테스트] 원자 소멸 시뮬레이션
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRFInKex8DFAUo

for tc in range(1, int(input()) + 1):
    n = int(input())
    atoms = [list(map(int, input().split())) for _ in range(n)]

    